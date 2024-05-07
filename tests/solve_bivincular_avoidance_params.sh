#!/bin/bash

# Solve patterns for bivincular avoidance. Put results in tests/output.
echo "== Solving all Params for Avoidance ==" && \
for file in tests/params/bivincular/avoidance/*
do
  conjure solve generic/models/pattern-type/bivincular-avoidance.essence "$file" --solver minion --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no -o tests/output/bivincular/avoidance
done

# Clean output directory to only contain JSON results.
echo "== Cleaning output ==" && \
find tests/output/bivincular/avoidance -type f ! -name '*.json' -delete