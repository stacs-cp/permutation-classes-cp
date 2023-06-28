import math

permset = []

# Create a set of all permutations which is global (permset) using Heap's algorithm
def genAllPerm(perm, length):
    if length == 1:
        permset.append(perm.copy())
    else:
        genAllPerm(perm, length-1)
    
    for i in range(0,length-1):
        tmp = perm[length-1]
        if (length % 2) == 0:
            perm[length-1] = perm[i]
            perm[i] = tmp
        else:
            perm[length-1] = perm[0]
            perm[0] = tmp
        genAllPerm(perm, length-1)

# For a given length generate all possible shadings. Which is in essence the power set of all coordinates.
def genAllMesh(length):
    coords = []
    # first the single regions
    for x in range(length+1):
        for y in range(length+1):
            coords.append([x,y])

    # Then create the powerset of those coordinates
    numSquares = len(coords)
    numMeshes = (int) (math.pow(2,len(coords)))
    shadings = []
    for count in range(numMeshes):
        tmp = []
        for i in range(numSquares):
            if ((count & (1 << i)) > 0):
                tmp.append(coords[i])    
        shadings.append(tmp)

    return shadings

# Generate all shadings for all permutations of a given length n. Which will be (n!*2^((n+1)^2)) 
def genAllPatterns(perm_length):
    genAllPerm([p+1 for p in range(perm_length)],perm_length)

    mesh = genAllMesh(perm_length)
    patts = []

    for i in permset:
        for j in mesh:
            patts.append([i,j])

    return patts


## Simple filters for possible coincidence
# the classic pattern has to be the same 
# Shading lemma
# def checkPerm(p1, p2):
#     return p1[0] == p2[0]

def generateParamFile(perm1, perm2)
    
    letting mesh_avoidance1 be (sequence(injective) of int, relation of (int * int))


$ The permutation we are searching for (1..length is the permutation)
given length : int


#plength = 2
for plength in range(1,5): 
    permset = []
    print(len(genAllPatterns(plength)))
# for i in a:
#     if i[0] == [1,2] and len(i[1]) == 2 and i[1][0] == [0,0]:
#         print(i)

#print(len(a))