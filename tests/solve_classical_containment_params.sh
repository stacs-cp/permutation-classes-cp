#!/bin/bash

# Solve patterns for classical containment. Put results in tests/output.
echo "== Solving all Params for Containment ==" && \
for file in tests/params/classical/containment/*
do
  conjure solve generic/models/pattern-type/classic-containment.essence "$file" --solver minion --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no -o tests/output/classical/containment
done

# Clean output directory to only contain JSON results.
echo "== Cleaning output ==" && \
find tests/output/classical/containment -type f ! -name '*.json' -delete