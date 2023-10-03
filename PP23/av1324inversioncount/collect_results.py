
import os
import json

allInfo = []

for dirpath, dirnames, filenames in os.walk("conjure-output"):
    for infofile in filenames:
        if infofile.endswith(".eprime-info"):
            [_, solver, length, nbInv] = infofile.split(".")[0].split("-")
            info = {}
            try:
                with open(f'{dirpath}/{infofile}', "r") as f:
                    for l in f:
                        [k, v] = l.split(":")
                        info[k.strip()] = v.strip()

                try:
                    info["TotalTime"] = str(
                        float(info["SolverTotalTime"]) + float(info["SavileRowTotalTime"]))
                except:
                    info["TotalTime"] = "NA"
            except FileNotFoundError:
                pass
            allInfo.append(([solver, length, nbInv], info))

headers = set()
for _, info in allInfo:
    headers = headers.union(info.keys())
headers = sorted(list(headers))

with open("outputs/info.csv", "w") as out:
    heading = ", ".join(["solver", "length", "nbInv"] + headers)
    print(heading, file=out)
    for [solver, length, nbInv], info in allInfo:
        print(", ".join([solver, length, nbInv] + [info[k] if k in info.keys() else "NA"
              for k in headers]), file=out)
