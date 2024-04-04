#!/bin/bash

echo "== Generating Classical Containment Params ==" && \
python3 tests/generate_params.py containment

echo "== Generating Classical Avoidance Params ==" && \
python3 tests/generate_params.py avoidance