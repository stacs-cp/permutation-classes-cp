#!/bin/bash

# Solve patterns for classical containment. Put results in tests/output.
echo "== Solving all Params for Containment ==" && \
for file in params/containment/*
do
  conjure solve ../generic/models/pattern-type/classic-containment.essence "$file" --solver minion --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no -o output/containment
done

# Clean output directory to only contain JSON results.
echo "== Cleaning output ==" && \
find output/containment -type f ! -name '*.json' -delete