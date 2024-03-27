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
    pattern_pairs = list(itertools.combinations(pattern, 2))
    permutation_pairs = list(itertools.combinations(permutation, 2))
    count = 0
    print("-------------------------")
    print("Permutation: ", permutation)
    print("Pattern: ", pattern_pairs)
    print("Permutation: ", permutation_pairs)
    for pair in pattern_pairs:
        for pair2 in permutation_pairs:
            height1 = pair[0] - pair[1]
            height2 = pair2[0] - pair2[1]
            if height1 == height2:
                permutation_pairs = permutation_pairs[permutation_pairs.index(pair2) + 1:]
                count += 1
                break

    if count == len(pattern_pairs):
        return True
    return False


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

    for permutation in itertools.permutations(range(1, len(pattern) + 2)):
        if check_permutation_is_contained(permutation, pattern):
            print("Checked Permutation:", permutation)


    '''
    for permutation in itertools.permutations(range(1, len(pattern) + 2)):
        if check_permutation_is_avoided(permutation, pattern):
            print("Checked Permutation:", permutation)
    '''

    # run_tests()

    '''
    print("-------------------------")
    print("Permutation: ", permutation)
    print("Pattern: ", pattern_pairs)
    print("Permutation: ", permutation_pairs)
    '''
