def sockMerchant(n, ar):
    sorted_list = sorted(ar)
    count = 0
    i = 0
    while i < (n - 1):
        if(sorted_list[i] == sorted_list[i + 1]):
             count += 1
             i = i + 2
        else:
            i = i + 1