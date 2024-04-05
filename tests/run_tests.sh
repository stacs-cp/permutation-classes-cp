#!/bin/bash

if [ "$1" = "classic" ]
  then
  if [ "$2" = "containment" ]
    then
      echo "== Running Test Suit on Classical Containment Results ==" && \
      python3 tests/classical_test.py containment
  elif [ "$2" = "avoidance" ]
    then
      echo "== Running Test Suit on Classical Avoidance Results ==" && \
      python3 tests/classical_test.py avoidance
  else
    echo "Not valid containment/avoidance!"
    exit 1
  fi
elif [ "$1" = "vincular" ]
  then
    if [ "$2" = "containment" ]
    then
      echo "== Running Test Suit on Vincular Containment Results ==" && \
      python3 tests/vincular_test.py containment 1
  elif [ "$2" = "avoidance" ]
    then
      echo "== Running Test Suit on Vincular Avoidance Results ==" && \
      python3 tests/vincular_test.py avoidance 1
  else
    echo "Not valid containment/avoidance!"
    exit 1
  fi
elif [ "$1" = "bivincular" ]
  then
    if [ "$2" = "containment" ]
    then
      echo "== Running Test Suit on Bivincular Containment Results ==" && \
      python3 tests/vincular_test.py containment 2
  elif [ "$2" = "avoidance" ]
    then
      echo "== Running Test Suit on Bivincular Avoidance Results ==" && \
      python3 tests/vincular_test.py avoidance 2
  else
    echo "Not valid containment/avoidance!"
    exit 1
  fi
else
  echo "Not a valid type!"
  exit 1
fi