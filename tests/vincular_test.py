import itertools
import json
import os
import re
import sys

from itertools import combinations


# Run all vincular tests
def run_tests(patternType):
    if patternType == 'containment':
        path = os.listdir('tests/output/vincular/containment')
        print("== Containment Check ==")
    else:
        path = os.listdir('tests/output/vincular/avoidance')
        print("== Avoidance Check ==")

    for filename in path:
        number = re.findall("[0-9]*-[0-9]", filename)
        index = number[0].index("-")
        pat = number[0][:index]
        pattern = []
        for x in pat:
            pattern.append(int(x))
        if patternType == 'containment':
            for adjacent in range(len(pattern)):
                containment_check(filename, pattern, adjacent)
        else:
            for adjacent in range(len(pattern)):
                avoidance_check(filename, pattern, adjacent)


# Check that all containment outputs have the right results
def containment_check(filename, pattern, adjacent):
    f = open('tests/output/vincular/containment/' + filename, 'r', encoding='utf')
    data = json.load(f)
    for entry in data:
        match check_permutation_is_contained(pattern, entry['perm'], adjacent):
            case True:
                continue
            case False:
                print("-- Pattern to Check: " + str(pattern) + " --")
                print("Permutation is invalid! {0}".format(entry['perm']))
                print("--------------------------------------------")


def check_permutation_is_contained(pattern, permutation, adjacent):
    pattern_pairs = list(itertools.combinations(pattern, len(pattern)))
    permutation_pairs = list(itertools.combinations(permutation, len(pattern)))

    for pair in permutation_pairs:
        if check_contain_pattern(pattern_pairs[0], pair, permutation, adjacent):
            return True
    return False


def check_contain_pattern(pattern_pairs, permutation_pairs, permutation, adjacent):
    patt_pairs = list(itertools.combinations(pattern_pairs, 2))
    perm_pairs = list(itertools.combinations(permutation_pairs, 2))
    patt_list = []
    perm_list = []
    for i in range(len(patt_pairs)):
        patt_list.append(patt_pairs[i][0] < patt_pairs[i][1])

    for i in range(len(perm_pairs)):
        perm_list.append(perm_pairs[i][0] < perm_pairs[i][1])

    return perm_list == patt_list and check_vincular_property(permutation_pairs, permutation, adjacent)


def check_vincular_property(permutation_pairs, permutation, adjacent):
    if permutation.index(permutation_pairs[adjacent]) - permutation.index(permutation_pairs[adjacent - 1]) == 1:
        return True
    return False


# Check that all avoidance outputs have the right results
def avoidance_check(filename, pattern, adjacent):
    f = open('tests/output/vincular/avoidance/' + filename, 'r', encoding='utf')
    data = json.load(f)
    for entry in data:
        match check_permutation_is_avoided(pattern, entry['perm'], adjacent):
            case True:
                continue
            case False:
                print("-- Pattern to Check: " + str(pattern) + " --")
                print("Permutation is invalid! {0}".format(entry['perm']))
                print("--------------------------------------------")


def check_permutation_is_avoided(pattern, permutation, adjacent):
    pattern_pairs = list(itertools.combinations(pattern, len(pattern)))
    permutation_pairs = list(itertools.combinations(permutation, len(pattern)))

    for pair in permutation_pairs:
        if check_avoid_pattern(pattern_pairs[0], pair, permutation, adjacent):
            return False
    return True


def check_avoid_pattern(pattern_pairs, permutation_pairs, permutation, adjacent):
    patt_pairs = list(itertools.combinations(pattern_pairs, 2))
    perm_pairs = list(itertools.combinations(permutation_pairs, 2))
    patt_list = []
    perm_list = []
    for i in range(len(patt_pairs)):
        patt_list.append(patt_pairs[i][0] < patt_pairs[i][1])

    for i in range(len(perm_pairs)):
        perm_list.append(perm_pairs[i][0] < perm_pairs[i][1])

    return perm_list == patt_list and check_vincular_property(perm_pairs, permutation, adjacent)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid arguments")
        print("Usage:", sys.argv[0], "<type> <containment/avoidance>")
        exit(1)
    run_tests(sys.argv[1])
