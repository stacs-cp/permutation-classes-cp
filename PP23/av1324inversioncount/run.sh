
mkdir -p params
mkdir -p outputs

# this is made for a large machine!
# 256 cores, 1TB memory

# populate conjure-output by running a small instance
rm -f conjure-output/model000001-minionseq-04-004.solutions.json.gz
python3 run.py minionseq 04 004

# generates commands-seq.txt and commands-par.txt
python3 gen_commands.py

# # seq
# parallel --no-notice -j240 \
#     --joblog outputs/gnuparallel-joblog-seq.tsv \
#     --results outputs/gnuparallel-results-seq \
#     --memfree 100G \
#     --shuf \
#     --eta \
#     :::: commands-seq.txt
# cat outputs/gnuparallel-joblog-seq.tsv | cut -f 1,4- > outputs/gnuparallel-joblog-seq.tsv.tmp ; mv outputs/gnuparallel-joblog-seq.tsv.tmp outputs/gnuparallel-joblog-seq.tsv

# par
parallel --no-notice -j1 \
    --joblog outputs/gnuparallel-joblog-par.tsv \
    --results outputs/gnuparallel-results-par \
    --memfree 100G \
    --eta \
    :::: commands-par.txt
cat outputs/gnuparallel-joblog-par.tsv | cut -f 1,4- > outputs/gnuparallel-joblog-par.tsv.tmp ; mv outputs/gnuparallel-joblog-par.tsv.tmp outputs/gnuparallel-joblog-par.tsv

# collect results
python3 collect_results.py
