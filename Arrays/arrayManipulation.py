
"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example:
n=10
queries = [[1,5,3], [4,8,7], [6,9,1]]

Queries are interpreted as follows
a b k
1 5 3
4 8 7
6 9 1

Add the values k between the indices a and b inclusive

index -> 1  2  3  4  5  6  7  8  9 10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        [3, 3, 3, 3, 3, 0, 0, 0, 0, 0]
        [3, 3, 3, 10,10,7, 7, 7, 0, 0]
        [3, 3, 3, 10,10,8, 8, 8, 1, 0]

You have to return the MAX value. In this case, it's 10.
"""

def arrayManipulation(n, queries):
    zeros = [[0 for j in range(n)] for i in range(3)]
    array = []
    pos = list()
    indices = dict()
    i = k = 0
    for j in queries:
        indices[i] = [j[0], j[1]]
        pos.append(j[2])
        i += 1

    for z in zeros:
        if k == 0:

            for s in range(indices[k][0] - 1, indices[k][1]):
                zeros[k][s] = pos[k]
            k += 1
        else:
            zeros[k] = zeros[k - 1].copy()
            for x in range(indices[k][0] - 1, indices[k - 1][1]):
                zeros[k][x] = pos[k-1] + pos[k]
            if k < 2:
                for x in range(indices[k + 1][0] -1, indices[k][1]):
                    zeros[k][x] = pos[k]
            else:
                for x in range(indices[k-1][1], indices[k][1]):
                    zeros[k][x] = pos[k]
            k+=1
    
    for i in zeros:
        for j in i:
            array.append(j)
    array.sort()
    return array.pop(), zeros
            
    


if __name__=='__main__':
    result = arrayManipulation(10, [[1,5,3], [4,8,7], [6,9,1]])
    print(result)