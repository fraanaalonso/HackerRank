from collections import defaultdict


def checkMagazine(magazine, note):
    d = defaultdict(int)
    for i in magazine:
        d[i]+=1
    for j in note:
        if d.get(j) is None or d[j] == 0:
            print('No')
            return
        else:
            d[j]-=1
    print('Yes')



string1 = 'give me one grand today night'
string2 = 'give one grand today today'

checkMagazine(string1.split(' '), string2.split(' '))
