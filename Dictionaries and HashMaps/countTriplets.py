def checkProgression(arr, r):
    for i in range(0, len(arr) - 1):
        if arr[i] * r == arr[i+1]:
            continue
        else:
            return False
    return True

def countTriplets(arr, r):
    d = dict()
    s = 0
    count = 0
    for i in range(0, len(arr) - 2):
        for j in range(i+1, len(arr) - 1):
            for k in range(j+1, len(arr)):
                d[s] = [arr[i], arr[j], arr[k]]
                s+=1

    for key, values in d.items():
        result = checkProgression(values, r)
        if result:
            count+=1


    return count



if __name__ == '__main__':
    result = countTriplets([1,3,9,9,27,81], 3)
    print(result)