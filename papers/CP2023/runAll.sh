
# populating the model cache
parallel --no-notice --joblog joblog --results results --eta bash run.sh ::: 4 3 2 1 ::: 5 ::: O0

# the real deal
parallel --no-notice --joblog joblog --results results --eta -j2 bash run.sh ::: 4 3 2 1 ::: $(seq 5 20) ::: O0

mkdir -p infos
cp output*/*info infos

