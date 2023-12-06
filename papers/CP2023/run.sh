
cp data.json data-$2-$1-$3.json
echo \""length\": $2}" >> data-$2-$1-$3.json
conjure solve $1.essence data-$2-$1-$3.json -o output-$1-$3 --solver minion --solver-options "-findallsols -noprintsols -cpulimit 3600" --savilerow-options -$3 +RTS -M128G

