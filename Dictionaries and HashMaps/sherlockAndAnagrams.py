def sherlockAndAnagrams(s):
    array = list(s)
    count = 0
    for i in range(0, len(array) -1):
        for j in range(0, len(array) -1):
            
            if array[i] == array[j+1]:
                count+=1
    
    return count


if __name__ == '__main__':
    done = sherlockAndAnagrams('abcd')
    print('Answer: ', done)