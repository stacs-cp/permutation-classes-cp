#!/bin/bash

if [ "$1" = "containment" ]
  then
    ./solve_classical_containment_params.sh
  else
    ./solve_classical_avoidance_params.sh
fi