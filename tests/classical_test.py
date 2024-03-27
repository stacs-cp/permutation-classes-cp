import itertools
import json
import os

# Run all classical tests
def run_tests():
    containment_files = os.listdir('output/containment')
    avoidance_files = os.listdir('output/avoidance/')

    for filename in containment_files:
        containment_check(filename)

    for filename in avoidance_files:
        avoidance_check(filename)

# Check that all containment outputs have the right results
def containment_check(filename):
    f = open('output/containment/' + filename, 'r', encoding='utf')
    data = json.load(f)
    for entry in data:
        match check_permutation_is_contained(entry['perm'], [1, 3, 2]):
            case True:
                continue
            case False:
                print("Permutation is invalid! {0}".format(entry['perm']))
                exit(0)

def check_permutation_is_contained(permutation, pattern):
    '''
    pattern_pairs = list(itertools.combinations(pattern, 2))
    permutation_pairs = list(itertools.combinations(permutation, 2))
    print("-------------------------")
    print("Permutation: ", permutation)
    print("Pattern: ", pattern_pairs)
    print("Permutation: ", permutation_pairs)
    count = 0
    for pair in pattern_pairs:
        for pair2 in permutation_pairs:
            if (pair[0] - pair[1] == pair2[0] - pair2[1]) ||
            if pair[0] - pair[1] == pair2[0] - pair2[1]:
                permutation_pairs = permutation_pairs[permutation_pairs.index(pair2) + 1:]
                count += 1
                break

    if count == len(pattern_pairs):
        return True
    return False
    '''
    pattern_pairs = list(itertools.combinations(pattern, 2))

    # Check each pair for relative order in the permutation
    for pair in pattern_pairs:
        found = False
        for i in range(len(permutation) - 1):
            if permutation[i] == pair[0]:
                for j in range(i + 1, len(permutation)):
                    if permutation[j] == pair[1]:
                        found = True
                        break
                if not found:
                    return False
                break
        if not found:
            return False

    return True

# Check that all avoidance outputs have the right results
def avoidance_check(filename):
    f = open('output/avoidance/' + filename, 'r', encoding='utf')
    data = json.load(f)
    for entry in data:
        print(entry['perm'])

def check_permutation_is_avoided(permutation, pattern):
    permutation_length = len(permutation)
    pattern_length = len(pattern)
    for i in range (permutation_length - pattern_length + 1):
        if not matches_pattern(permutation[i:i + pattern_length], pattern):
            continue
        else:
            return False
    return True

def matches_pattern(subsequence, pattern):
    pattern_index = 0
    for element in subsequence:
        if element == pattern[pattern_index]:
            pattern_index += 1
            if pattern_index == len(pattern):
                return True
    return False


if __name__ == '__main__':
    pattern = [1, 3, 2]
    '''
    for permutation in itertools.permutations(range(1, len(pattern) + 2)):
        if check_permutation_is_contained(permutation, pattern):
            print("Checked Permutation:", permutation)
    '''

    for permutation in itertools.permutations(range(1, len(pattern) + 2)):
        if check_permutation_is_avoided(permutation, pattern):
            print("Checked Permutation:", permutation)
    # run_tests()

    '''
    print("-------------------------")
    print("Permutation: ", permutation)
    print("Pattern: ", pattern_pairs)
    print("Permutation: ", permutation_pairs)
    '''
