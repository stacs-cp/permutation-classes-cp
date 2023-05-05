
cp data.json data-$1-$2-$3.json
echo \""length\": $1}" >> data-$1-$2-$3.json
conjure solve $2.essence data-$1-$2-$3.json -o output-$2-$3 --solver minion --solver-options "-findallsols -noprintsols" --savilerow-options -$3

