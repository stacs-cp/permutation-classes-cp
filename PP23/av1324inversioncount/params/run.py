from generate import *

test = True

if test:
    mp = [True,4]
    run([0,5],5,mp)
else:
    maxlength = 20
    inversionrange = [0,comb(maxlength,2)]
    mp = [True,4]
    run(inversionrange,maxlength,mp)





#combinesols(inversionrange)
