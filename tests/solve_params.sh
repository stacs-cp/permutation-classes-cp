#!/bin/bash

if [ "$1" = "classic" ]
  then
  if [ "$2" = "containment" ]
    then
      ./tests/solve_classical_containment_params.sh
  elif [ "$2" = "avoidance" ]
    then
      ./tests/solve_classical_avoidance_params.sh
  else
    echo "Not valid containment/avoidance!"
    exit 1
  fi
elif [ "$1" = "vincular" ]
  then
    if [ "$2" = "containment" ]
    then
      ./tests/solve_vincular_containment_params.sh
  elif [ "$2" = "avoidance" ]
    then
      ./tests/solve_vincular_avoidance_params.sh
  else
    echo "Not valid containment/avoidance!"
    exit 1
  fi
elif [ "$1" = "bivincular" ]
  then
    if [ "$2" = "containment" ]
    then
      ./tests/solve_bivincular_containment_params.sh
  elif [ "$2" = "avoidance" ]
    then
      ./tests/solve_bivincular_avoidance_params.sh
  else
    echo "Not valid containment/avoidance!"
    exit 1
  fi
else
  echo "Not a valid type!"
  exit 1
fi