def countingValleys(steps, path):
    st = list(path)
    position = 0
    count = 0
    last = ''
    
    for i in range(0, steps):
        if(st[i] == 'U'):
            position+=1
        else:
            position-=1
        last = st[i]
        if(position == 0 and last != 'D'):
            count+=1
    return count