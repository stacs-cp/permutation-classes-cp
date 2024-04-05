# Commands:

### Find solutions -
```console
conjure solve foo.essence bar.param --solver minion --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no
```

### Change output directory -
```console
conjure solve foo.essence bar.param --solver minion --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no -o output
```

### Print statements for testing code -
```console
pattern = [1, 3, 2]
    count = 0

    for permutation in itertools.permutations(range(1, len(pattern) + 2)):
        if check_permutation_is_contained(pattern, permutation, 2):
            print("Checked Permutation:", permutation)
            count += 1
    print(count)
```