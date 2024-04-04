import json
import sys
from itertools import permutations


def generate_params(type, subType):
    # Determine Pattern Type
    match type:
        case "classic":
            match subType:
                case "containment":
                    path = "tests/params/classical/containment/"
                case "avoidance":
                    path = "tests/params/classical/avoidance/"
                case _:
                    print("Unrecognized subType!")
                    exit(1)
        case "vincular":
            match subType:
                case "containment":
                    path = "tests/params/vincular/containment/"
                case "avoidance":
                    path = "tests/params/vincular/avoidance/"
                case _:
                    print("Unrecognized subType!")
                    exit(1)
        case _:
            print("Unrecognized type!")
            exit(1)

    # Generate Permutations up to length 6 and write to directory
    for length in range(1, 6):
        for perm in permutations(range(1, length + 1)):
            permutation = toString(perm)
            for length_of_perm in range(length, 6):
                f = open(path + "classic" + permutation + "-" + str(length_of_perm) + ".json", 'w')
                match type:
                    case "classic":
                        pattern = {"length": length_of_perm, type + "_" + subType: [perm,]}
                    case "vincular":
                        pattern = {"length": length_of_perm, type + "_" + subType: [perm, [1]]}
                json_pattern = json.dumps(pattern, indent=4)
                with f as outfile:
                    outfile.write(json_pattern)

def toString(perm):
    s = ''.join(map(str, perm))
    return s

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Invalid arguments")
        print("Usage:", sys.argv[0], "<type> <containment/avoidance")
        exit(1)
    generate_params(sys.argv[1], sys.argv[2])
