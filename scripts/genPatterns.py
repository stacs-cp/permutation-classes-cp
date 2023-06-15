import math

permset = []

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

def genAllMesh(length):
    coords = []
    for x in range(length+1):
        for y in range(length+1):
            coords.append([x,y])

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

def genAllPatterns(perm_length):
    genAllPerm([p+1 for p in range(perm_length)],perm_length)

    mesh = genAllMesh(perm_length)
    patts = []

    for i in permset:
        for j in mesh:
            patts.append([i,j])

    return patts


plength = 2
a = genAllPatterns(plength)
for i in a:
    print(i)
