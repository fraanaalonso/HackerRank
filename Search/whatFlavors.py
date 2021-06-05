#less efficient: more complexity
def whatFlavors1(cost, money):
    for i in range(0, len(cost)):
        for j in range(i + 1, len(cost)):
            if cost[i] + cost[j] == money:
                x = f'{i+1} {j+1}'
    
    print(x)

def whatFlavors(cost, money):
    cost_dict = {}
    for i,icost in enumerate(cost):
        if money-icost in cost_dict:
            print(str(cost_dict[money-icost]+1) + ' ' + str(i+1))
            return 
        else:
            cost_dict[icost] = i

if __name__ == '__main__':
        print(whatFlavors([2,1,3,5,6], 5))