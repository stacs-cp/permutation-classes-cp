To run all instances from the json file:

    (time python3 -u run.py) 2>&1 | tee stdout.txt


To run a single instance:

    conjure solve pc.essence params/0012.param --number-of-solutions=all


