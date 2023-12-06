moving to the composable-permutation-patterns repo:

- copy everything
- only keep the minionpar results
- remove Solver*Time fields from the info files as minion's time reporting is kaput for parallel
- inside conjure-output: parallel "grep -v 'SolverTotalTime\|SolverSolveTime\|SolverSetupTime' {} > {}.out" ::: *info
- inside conjure-output: parallel "mv {} {.}" ::: *.out
- rerun: python3 collect_results.py

