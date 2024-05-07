#!/bin/bash

# Solve patterns for vincular avoidance. Put results in tests/output.
echo "== Solving all Vincular Params for avoidance ==" && \
for file in tests/params/vincular/avoidance/*
do
  conjure solve generic/models/pattern-type/vincular-avoidance.essence "$file" --solver minion --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no -o tests/output/vincular/avoidance
done

# Clean output directory to only contain JSON results.
echo "== Cleaning output ==" && \
find tests/output/vincular/avoidance -type f ! -name '*.json' -delete