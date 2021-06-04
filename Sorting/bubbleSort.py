


def countSwaps(a):
    aux = 0
    count = 0
    for i in range(0, len(a)):
        for j in range(0, len(a) - 1):
            if a[j] > a[j + 1]:
                aux = a[j]
                a[j] = a[j+1]
                a[j + 1] = aux
                count += 1
    return [count, a[0], a[len(a) - 1]]

if __name__ == '__main__':
    a = [1, 2, 3]
    result = countSwaps(a)

    print(f'Array is sorted in {result[0]} swaps')
    print(f'First element: {result[1]}')
    print(f'Last element: {result[2]}')