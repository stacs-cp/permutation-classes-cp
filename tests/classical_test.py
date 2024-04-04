import itertools
import json
import os
import re

from itertools import combinations


# Run all classical tests
def run_tests():
    containment_files = os.listdir('tests/output/classical/containment')
    avoidance_files = os.listdir('tests/output/classical/avoidance')

    print("== Containment Check ==")
    for filename in containment_files:
        number = re.findall("[0-9]*-[0-9]", filename)
        index = number[0].index("-")
        pat = number[0][:index]
        pattern_to_contain = []
        for x in pat:
            pattern_to_contain.append(int(x))
        containment_check(filename, pattern_to_contain)

    print("== Avoidance Check ==")
    for filename in avoidance_files:
        number = re.findall("[0-9]*-[0-9]", filename)
        index = number[0].index("-")
        pat = number[0][:index]
        pattern_to_avoid = []
        for x in pat:
            pattern_to_avoid.append(int(x))
        avoidance_check(filename, pattern_to_avoid)


# Check that all containment outputs have the right results
def containment_check(filename, pattern):
    f = open('output/classical/containment/' + filename, 'r', encoding='utf')
    data = json.load(f)
    for entry in data:
        match check_permutation_is_contained(pattern, entry['perm']):
            case True:
                continue
            case False:
                print("== Pattern to Check: " + str(pattern) + " ==")
                print("Permutation is invalid! {0}".format(entry['perm']))
                print("============================================")


def check_permutation_is_contained(pattern, permutation):
    pattern_pairs = list(itertools.combinations(pattern, len(pattern)))
    permutation_pairs = list(itertools.combinations(permutation, len(pattern)))

    for pair in permutation_pairs:
        if check_contain_pattern(pattern_pairs[0], pair):
            return True
    return False

def check_contain_pattern(pattern_pairs, permutation_pairs):
    patt_pairs = list(itertools.combinations(pattern_pairs, 2))
    perm_pairs = list(itertools.combinations(permutation_pairs, 2))
    patt_list = []
    perm_list = []
    for i in range(len(patt_pairs)):
        patt_list.append(patt_pairs[i][0] < patt_pairs[i][1])

    for i in range(len(perm_pairs)):
        perm_list.append(perm_pairs[i][0] < perm_pairs[i][1])

    return perm_list == patt_list


# Check that all avoidance outputs have the right results
def avoidance_check(filename, pattern):
    f = open('output/classical/avoidance/' + filename, 'r', encoding='utf')
    data = json.load(f)
    for entry in data:
        match check_permutation_is_avoided(pattern, entry['perm']):
            case True:
                continue
            case False:
                print("== Pattern to Check: " + str(pattern) + " ==")
                print("Permutation is invalid! {0}".format(entry['perm']))
                print("============================================")


def check_permutation_is_avoided(pattern, permutation):
    pattern_pairs = list(itertools.combinations(pattern, len(pattern)))
    permutation_pairs = list(itertools.combinations(permutation, len(pattern)))

    for pair in permutation_pairs:
        if check_avoid_pattern(pattern_pairs[0], pair):
            return False
    return True

def check_avoid_pattern(pattern_pairs, permutation_pairs):
    patt_pairs = list(itertools.combinations(pattern_pairs, 2))
    perm_pairs = list(itertools.combinations(permutation_pairs, 2))
    patt_list = []
    perm_list = []
    for i in range(len(patt_pairs)):
        patt_list.append(patt_pairs[i][0] < patt_pairs[i][1])

    for i in range(len(perm_pairs)):
        perm_list.append(perm_pairs[i][0] < perm_pairs[i][1])

    return perm_list == patt_list


if __name__ == '__main__':
    run_tests()
