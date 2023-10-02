
# Solvers:
# - minionseq
# - minionpar
# - nbcsat

# Length:
# - 4 to 25

# Number of inversions:
# - 0 .. comb(length,2)

import math

for solver in ["minionseq", "nbcsat"]:
    for length in range(1, 20+1):
        lengthPadded = str(length).zfill(2)
        for nbInv in range(0, math.comb(length, 2) + 1):
            nbInvPadded = str(nbInv).zfill(2)
            print(f'python3 run.py {solver} {lengthPadded} {nbInvPadded}')
