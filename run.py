import json, subprocess, sys, csv, time

jsonFile = "result-known.json"
solver = sys.argv[1]

def log(s):
    print("LOG: %s" % s)

def save(fieldNames, stats):
    with open("logs-%s.csv" % solver, "w") as csvfile:
        writer = csv.DictWriter( csvfile, fieldNames
                               , delimiter = ','
                               , quotechar = '"'
                               , quoting = csv.QUOTE_MINIMAL
                               )
        writer.writeheader()
        for _, pStats in stats.items():
            writer.writerow(pStats)



# Convert to param files
################################################################################

knownSolutions = {}
paramFiles = []
with open(jsonFile, "r") as inp:
    raw = json.load(inp)
    for obj in raw:
        avoiding = obj["avoiding"]
        length = obj["length"]
        result = obj["result"]
        formula = obj["formula"]

        name = "-".join([ "".join([str(x) for x in av]) for av in avoiding ])
        name = "%s--%03d" % (name, length)

        paramFile = "params/%s.param" % name
        paramFiles.append("%s" % name)
        knownSolutions["%s" % name] = result

        with open(paramFile, "w") as out:
            print("language Essence 1.3", file=out)
            print("", file=out)
            print("$ formula: ", formula, file=out)
            print("$ result: ", result, file=out)
            print("", file=out)
            print("letting length be", length, file=out)
            avoidingStr = "{" + ", ".join([ "sequence(" + ",".join([str(x) for x in av]) +  ")" for av in avoiding ]) + "}"
            print("letting avoiding be", avoidingStr, file=out)
log("Generated param files")


# Generate E'
subprocess.run(["rm", "-rf", "conjure-output"])
subprocess.run(["conjure", "modelling", "pc.essence", "-o", "conjure-output"])
log("Generated E'")



# Solve
################################################################################

stats = {}
fieldNames = [ "instance"
             , "solver"
             , "Wall time - Conjure translate param"
             , "Wall time - Savile Row"
             , "Wall time - Solver"
             , "correct"
             , "Total Nodes"
             , "Solutions Found"
             ]



for paramFile in paramFiles:
    stats[paramFile] = {}
    stats[paramFile]["instance"] = paramFile

    startTime = time.time()
    subprocess.run([ "conjure"
                   , "translate-param"
                   , "--eprime", "conjure-output/model000001.eprime"
                   , "--essence-param", "params/%s.param" % paramFile
                   , "--eprime-param", "conjure-output/%s.param" % paramFile
                   ], capture_output=True)
    stats[paramFile]["Wall time - Conjure translate param"] = " %.2f" % (time.time() - startTime)

    if solver == "minion":
        stats[paramFile]["solver"] = "minion"
        startTime = time.time()
        subprocess.run([ "savilerow"
                       , "conjure-output/model000001.eprime"
                       , "conjure-output/%s.param" % paramFile
                       , "-timelimit", "120"
                       ], capture_output=True)
        stats[paramFile]["Wall time - Savile Row"] = " %.2f" % (time.time() - startTime)

        startTime = time.time()
        out = subprocess.run([ "minion"
                             , "-findallsols"
                             , "-noprintsols"
                             , "-cpulimit", "120"
                             , "conjure-output/%s.param.minion" % paramFile
                             ], capture_output=True)
        stats[paramFile]["Wall time - Solver"] = " %.2f" % (time.time() - startTime)
    elif solver == "sat":
        stats[paramFile]["solver"] = "sat"
        startTime = time.time()
        subprocess.run([ "savilerow"
                       , "conjure-output/model000001.eprime"
                       , "conjure-output/%s.param" % paramFile
                       , "-sat"
                       , "-timelimit", "120"
                       ], capture_output=True)
        stats[paramFile]["Wall time - Savile Row"] = " %.2f" % (time.time() - startTime)

        startTime = time.time()
        out = subprocess.run([ "nbc_minisat_all_release"
                             , "conjure-output/%s.param.dimacs" % paramFile
                             ], capture_output=True)
        stats[paramFile]["Wall time - Solver"] = " %.2f" % (time.time() - startTime)

    stdoutLines = out.stdout.decode("utf-8").split("\n")

    # capturing the output
    for l in stdoutLines:
        parts = l.split(":")
        if len(parts) == 2:
            parts[0] = parts[0].strip()
            if parts[0] == "SAT (full)":
                parts[0] = "Solutions Found"
        if parts[0] in fieldNames:
            stats[paramFile][parts[0]] = parts[1]

    # some logging
    if "Solutions Found" in stats[paramFile].keys():
        nbSolutions = stats[paramFile]["Solutions Found"]
        if knownSolutions[paramFile] == "Unknown":
            log("Done %s. Found %d solutions." % (paramFile, nbSolutions))
            stats[paramFile]["correct"] = "Not checked"
        else:
            nbSolutions = int(nbSolutions)
            if nbSolutions == knownSolutions[paramFile]:
                log("Done %s. Correct solution found." % paramFile)
                stats[paramFile]["correct"] = "Correct"
            else:
                log("Done %s. Incorrect solution found. Expected %d, but got %d." % (paramFile, knownSolutions[paramFile], nbSolutions))
                stats[paramFile]["correct"] = "Incorrect"
    else:
        log("Done %s. Expected %s, found NONE." % (paramFile, knownSolutions[paramFile]))
        stats[paramFile]["correct"] = "Not found"        

    save(fieldNames, stats)



# Save stats to file
################################################################################

save(fieldNames, stats)

