def minimumSwaps(arr):
    #arr = [7,1,3,2,4,5,6]
    n = len(arr) #7
    arrpos = [*enumerate(arr)] # arrpos = [(0,7),(1,1), (2,3), (2,2), (2,4), (2,5), (2,6)]
    
    arrpos.sort(key = lambda pos : pos[1])
    vis = {l : 0 for l in range(n)}
     
    res = 0
    for i in range(n):
        k = 0
        j = i        
        while vis[j] == 0:            
            vis[j] = 1
            j = arrpos[j][0]
            k += 1
        if k > 0:
            res += (k - 1)
    return res



if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    result = minimumSwaps(q)
    print('Minimum Swaps: ', result)