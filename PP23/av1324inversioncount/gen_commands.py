import math
import os

# Solvers:
# - minionseq
# - minionpar
# - nbcsat

# Length:
# - 1 to upto
upto = 15

# Number of inversions:
# - 0 .. comb(length,2)


with open("commands-seq.txt", "w") as out:
    for solver in ["minionseq", "nbcsat"]:
        for length in range(1, upto+1):
            lengthPadded = str(length).zfill(2)
            for nbInv in range(0, math.comb(length, 2) + 1):
                nbInvPadded = str(nbInv).zfill(3)
                solutionFile = f'gzip conjure-output/model000001-{solver}-{lengthPadded}-{nbInvPadded}.solutions.json.gz'
                if not os.path.exists(solutionFile):
                    print(
                        f'python3 run.py {solver} {lengthPadded} {nbInvPadded}', file=out)

with open("commands-par.txt", "w") as out:
    for solver in ["minionpar"]:
        for length in range(1, upto+1):
            lengthPadded = str(length).zfill(2)
            for nbInv in range(0, math.comb(length, 2) + 1):
                nbInvPadded = str(nbInv).zfill(3)
                solutionFile = f'gzip conjure-output/model000001-{solver}-{lengthPadded}-{nbInvPadded}.solutions.json.gz'
                if not os.path.exists(solutionFile):
                    print(
                        f'python3 run.py {solver} {lengthPadded} {nbInvPadded}', file=out)
