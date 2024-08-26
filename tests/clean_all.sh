#!/bin/bash

echo "== Cleaning Classical Params ==" && \
rm -r tests/params/classical/containment/* && \
rm -r tests/params/classical/avoidance/*

echo "== Cleaning Classical Output ==" && \
rm -r tests/output/classical/containment/* && \
rm -r tests/output/classical/avoidance/*

echo "== Cleaning Vincular Params ==" && \
rm -r tests/params/vincular/containment/* && \
rm -r tests/params/vincular/avoidance/*

echo "== Cleaning Vincular Output ==" && \
rm -r tests/output/vincular/containment/* && \
rm -r tests/output/vincular/avoidance/*