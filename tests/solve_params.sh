#!/bin/bash

if [ "$1" = "containment" ]
  then
    ./tests/solve_classical_containment_params.sh
  else
    ./tests/solve_classical_avoidance_params.sh
fi