#!/bin/bash

# Solve patterns for vincular containment. Put results in tests/output.
echo "== Solving all Params for Containment ==" && \
for file in tests/params/vincular/containment/*
do
  conjure solve generic/models/pattern-type/vincular-containment.essence "$file" --solver minion --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no -o tests/output/vincular/containment
done

# Clean output directory to only contain JSON results.
echo "== Cleaning output ==" && \
find tests/output/vincular/containment -type f ! -name '*.json' -delete