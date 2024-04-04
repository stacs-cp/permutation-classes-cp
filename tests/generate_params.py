import json
import sys
from itertools import permutations


def generate_params(type):
    # Determine Pattern Type
    match type:
        case "containment":
            path = "params/classical/containment/"
        case "avoidance":
            path = "params/classical/avoidance/"

    # Generate Permutations up to length 6 and write to directory
    for length in range(1, 7):
        for perm in permutations(range(1, length + 1)):
            permutation = toString(perm)
            for length_of_perm in range(length, 7):
                f = open(path + "classic" + permutation + "-" + str(length_of_perm) + ".json", 'w')
                pattern = {"length": length_of_perm, "classic_" + type: [perm]}
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