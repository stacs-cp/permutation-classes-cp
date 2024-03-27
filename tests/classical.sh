#!/bin/bash

# Solve patterns for classical containment. Put results in tests/output.
conjure solve ../generic/models/pattern-type/classic-containment.essence ../generic/params/containment/classic132.json --solver minion --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no -o output/containment

# Solve patterns for classical avoidance. Put results in tests/output.
conjure solve ../generic/models/pattern-type/classic-avoidance.essence ../generic/params/avoidance/classic132.param --solver minion --number-of-solutions=all --output-format=json --solutions-in-one-file --copy-solutions=no -o output/avoidance

# Clean output directory to only contain JSON results.
find output -type f ! -name '*.json' -delete

# Run python testing for classical containment and avoidance
python3 classical_test.py