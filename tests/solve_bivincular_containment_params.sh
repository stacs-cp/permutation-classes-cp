#!/bin/bash

# Solve patterns for bivincular containment. Put results in tests/output.
echo "== Solving all Params for Avoidance ==" && \
for file in tests/params/bivincular/containment/*
do
  conjure solve generic/models/pattern-type/bivincular-containment.essence "$file" --solver minion --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no -o tests/output/bivincular/containment
done

# Clean output directory to only contain JSON results.
echo "== Cleaning output ==" && \
find tests/output/bivincular/containment -type f ! -name '*.json' -delete