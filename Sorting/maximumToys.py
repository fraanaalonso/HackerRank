
def maximumToys(prices, k):
    prices.sort()
    i = 0
    totalPayment = 0
    toys= []
    while i < len(prices) - 1 and totalPayment <= k:
        if not (totalPayment + prices[i] > k):
            toys.append(prices[i])
            totalPayment += prices[i]

        i+=1
    
    return len(toys)

if __name__ == '__main__':
    prices = [1, 2, 3, 4]
    k = 7
    result = maximumToys(prices, k)

    print(result)