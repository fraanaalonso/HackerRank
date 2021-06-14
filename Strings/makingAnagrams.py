


def makeAnagram(a, b):
    array1 = list(a)
    array2 = list(b)
    deletions = 0
    x = array1.copy()
    y = array2.copy()

    for i in array1:
        if i not in array2:
            deletions+=1
            x.remove(i)
    for j in array2:
        if j not in array1:
            deletions+=1
            y.remove(j)
            
    

    
    
    

    print(x)
    print(y)
    return deletions

if __name__ == '__main__':
    result = makeAnagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke')
    print(result)