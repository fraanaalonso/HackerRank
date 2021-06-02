def twoStrings(s1, s2):
    a = set(list(s1)) 
    b = set(list(s2)) 
    isRep = a.intersection(b) 
    if len(isRep) > 0: 
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    done = twoStrings('hello', 'world')
    undone = twoStrings('hi', 'world')
    print('Answer: ', done)
    print('Answer: ', undone)