#!/bin/bash

if [ "$1" = "classic" ]
  then
  if [ "$2" = "containment" ]
    then
      echo "== Generating Classical Containment Params ==" && \
      python3 tests/generate_params.py classic containment
  elif [ "$2" = "avoidance" ]
    then
      echo "== Generating Classical Avoidance Params ==" && \
      python3 tests/generate_params.py classic avoidance
  else
    echo "Not valid containment/avoidance!"
    exit 1
  fi
elif [ "$1" = "vincular" ]
  then
    if [ "$2" = "containment" ]
    then
      echo "== Generating Vincular Containment Params ==" && \
      python3 tests/generate_params.py vincular containment
  elif [ "$2" = "avoidance" ]
    then
      echo "== Generating Vincular Avoidance Params ==" && \
      python3 tests/generate_params.py vincular avoidance
  else
    echo "Not valid containment/avoidance!"
    exit 1
  fi
else
  echo "Not a valid type!"
  exit 1
fi