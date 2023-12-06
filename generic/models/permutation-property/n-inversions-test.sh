pushd models/permutation-property

for length in $(seq 3 5); do
    for nInversions in 0 3 7; do
        echo "{\"length\": $length, \"nInversions\": $nInversions, \"turnedOn\": true}" > n-inversions-$length-$nInversions.json
        conjure solve n-inversions.essence n-inversions-$length-$nInversions.json --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no -o co-n-inversions
        python3 n-inversions-test.py n-inversions-$length-$nInversions.json co-n-inversions/model000001-n-inversions-$length-$nInversions.solutions.json
        rm -f n-inversions-$length-$nInversions.json
    done
done

rm -rf co-n-inversions

popd
