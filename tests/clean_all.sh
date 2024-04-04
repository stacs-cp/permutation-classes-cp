#!/bin/bash

echo "== Cleaning Classical Params ==" && \
rm -r params/classical/containment/* && \
rm -r params/classical/avoidance/*

echo "== Cleaning Classical Output ==" && \
rm -r output/classical/containment/* && \
rm -r output/classical/avoidance/*