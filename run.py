import json

with open("seqwiki.json", "r") as inp:
    raw = json.load(inp)
    for n, obj in enumerate(raw):
        avoiding = obj["avoiding"]
        length = obj["length"]
        result = obj["result"]
        formula = obj["formula"]

        with open("params/%04d.param" % n, "w") as out:
            print("language Essence 1.3", file=out)
            print("", file=out)
            print("$ formula: ", formula, file=out)
            print("$ result: ", result, file=out)
            print("", file=out)
            print("letting length be", length, file=out)
            print("letting avoiding be", avoiding, file=out)
