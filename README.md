
To run all instances from the json file:

    (time python3 -u run.py minion) 2>&1 | tee stdout-minion.txt
    (time python3 -u run.py sat) 2>&1 | tee stdout-sat.txt


To run a single instance:

    conjure solve pc.essence params/0012.param --number-of-solutions=all


