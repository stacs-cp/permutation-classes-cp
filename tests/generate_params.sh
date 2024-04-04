#!/bin/bash

echo "== Generating Classical Containment Params ==" && \
python3 tests/generate_params.py classic containment

echo "== Generating Classical Avoidance Params ==" && \
python3 tests/generate_params.py classic avoidance

echo "== Generating Vincular Containment Params ==" && \
python3 tests/generate_params.py vincular containment

echo "== Generating Vincular Avoidance Params ==" && \
python3 tests/generate_params.py vincular avoidance