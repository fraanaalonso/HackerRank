from collections import defaultdict

def riddle(arr):
    k = 0
    d = defaultdict(list)
    aux = defaultdict(int)

    for i in range(1, len(arr) + 1):
        b = list()
        for j in range(i, len(arr) + 1):
            if i == 1:
                b.append(max(arr))
            else:
                b.append(arr[k:j])
            k+=1
        d[i]=b
        k = 0
    arr = []
    for key, value in d.items():
        if key == 1:
            aux[key] = max(value)
        else:
            for i in range(0, len(value)):
                arr.append(min(value[i]))
            aux[key] = max(arr)
            arr.clear()
    
    return aux.values()

print(riddle([6, 3, 5, 1, 12]))
print(riddle([2, 6, 1, 12]))
print(riddle([1, 2, 3, 5, 1, 13, 3]))
print(riddle([3, 5, 4, 7, 6, 2]))