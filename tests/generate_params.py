import json
import sys
from itertools import permutations


def generate_params(type):
    # Determine Pattern Type
    match type:
        case "containment":
            path = "params/containment/"
        case "avoidance":
            path = "params/avoidance/"

    # Generate Permutations up to length 6 and write to directory
    for length in range(1, 6):
        for perm in permutations(range(1, length + 1)):
            permutation = toString(perm)
            f = open(path + "classic" + permutation + ".json", 'w')
            pattern = {"length": length, "classic_" + type: [perm]}
            json_pattern = json.dumps(pattern, indent=4)
            with f as outfile:
                outfile.write(json_pattern)

def toString(perm):
    s = ''.join(map(str, perm))
    return s

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid arguments")
        print("Usage:", sys.argv[0], "<patternType>")
        exit(1)
    generate_params(sys.argv[1])