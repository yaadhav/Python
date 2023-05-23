def solve(s):
    i=0
    count=''
    spaces=[]

    while i<len(s):
        while not s[i].isalnum() and i<len(s):
            count+=s[i]
            i+=1
        if count!='':
            spaces.append(count)
            count=''
        i+=1

    words=s.split()
    res=words[0].capitalize()
    for i in range(1, len(words)):
        res+=spaces[i-1]+words[i].capitalize()
    
    return res

'''
#Alternate Solution

def solve(s):
    return s.title()
'''

if __name__ == '__main__':
    s = input()
    print(solve(s))

