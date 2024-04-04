#!/bin/bash

# Run python testing for classical containment and avoidance
echo "== Running Test Suit on Classical Containment Results ==" && \
python3 tests/classical_test.py containment

echo "== Running Test Suit on Classical Avoidance Results ==" && \
python3 tests/classical_test.py avoidance