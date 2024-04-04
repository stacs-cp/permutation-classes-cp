#!/bin/bash

if [ "$1" = "containment" ]
  then
    ./tests/solve_classical_containment_params.sh
elif [ "$1" = "avoidance" ]
  then
    ./tests/solve_classical_avoidance_params.sh
else
  echo "Not a valid option!"
  exit 1
fi