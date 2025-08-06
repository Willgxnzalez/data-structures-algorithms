def convertToTuple(num):
    numStr = str(num).zfill(3)
    return tuple(map(int, numStr))

def convertToInt(tup):
    numStr = "".join(map(str, tup))
    return int(numStr)

def radixSort(A):
    A = [convertToTuple(x) for x in A]
    for field in range(2,-1,-1):
        A.sort(key = lambda x: x[field])
    
    return [convertToInt(x) for x in A]

print(radixSort([435, 234, 100, 34, 19, 183]))
