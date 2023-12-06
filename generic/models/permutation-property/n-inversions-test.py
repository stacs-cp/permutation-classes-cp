import sys
import json

with open(sys.argv[1], "r") as f:
    param = json.load(f)

with open(sys.argv[2], "r") as f:
    solutions = json.load(f)

print(f'Testing {sys.argv}')

for solution in solutions:
    length = param["length"]
    nInversions = param["nInversions"]
    perm = solution["perm"]

    if not len(perm) == length:
        print(f"{sys.argv} -- Expected length {length}, but got: {len(perm)} -- {perm}", file=sys.stderr)

    count = sum([1 for i in range(length)
                 for j in range(length)
                 if all([i < j, perm[i] > perm[j]])
                 ])

    if not nInversions == count:
        print(f"{sys.argv} -- Expected nInversions {nInversions}, but got: {count} -- {perm}", file=sys.stderr)
