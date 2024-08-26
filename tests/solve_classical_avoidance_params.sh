#!/bin/bash

# Solve patterns for classical avoidance. Put results in tests/output.
echo "== Solving all Params for Avoidance ==" && \
for file in tests/params/classical/avoidance/*
do
  conjure solve generic/models/pattern-type/classic-avoidance.essence "$file" --solver minion --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no -o tests/output/classical/avoidance
done

# Clean output directory to only contain JSON results.
echo "== Cleaning output ==" && \
find tests/output/classical/avoidance -type f ! -name '*.json' -delete