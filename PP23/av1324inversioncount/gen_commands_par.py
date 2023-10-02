
# Solvers:
# - minionseq
# - minionpar
# - nbcsat

# Length:
# - 4 to 25

# Number of inversions:
# - 0 .. comb(length,2)

import math

for solver in ["minionpar"]:
    for length in [7]:  # range(4, 20+1):
        for nbInv in range(0, math.comb(length, 2) + 1):
            print(f'python3 run.py {solver} {length} {nbInv}')
