#!/bin/bash

if [ "$1" = "classic" ]
  then
  if [ "$2" = "containment" ]
    then
      mkdir -p tests/params/classical/containment
      mkdir -p tests/output/classical/containment
  elif [ "$2" = "avoidance" ]
    then
      mkdir -p tests/params/classical/avoidance
      mkdir -p tests/output/classical/avoidance
  else
    echo "Not valid containment/avoidance!"
    exit 1
  fi
elif [ "$1" = "vincular" ]
  then
    if [ "$2" = "containment" ]
    then
      mkdir -p tests/params/vincular/containment
      mkdir -p tests/output/vincular/containment
  elif [ "$2" = "avoidance" ]
    then
      mkdir -p tests/params/vincular/avoidance
      mkdir -p tests/output/vincular/avoidance
  else
    echo "Not valid containment/avoidance!"
    exit 1
  fi
elif [ "$1" = "bivincular" ]
  then
    if [ "$2" = "containment" ]
      then
        mkdir -p tests/params/bivincular/containment
        mkdir -p tests/output/bivincular/containment
  elif [ "$2" = "avoidance" ]
    then
      mkdir -p tests/params/bivincular/avoidance
      mkdir -p tests/output/bivincular/avoidance
  else
    echo "Not valid containment/avoidance!"
    exit 1
  fi
else
  echo "Not a valid type!"
  exit 1
fi