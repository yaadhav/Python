def length(list):
    res=[]
    for word in list:
        a=len(word)
        while a>0:
            res.append(word[0:a])
            a-=1
    return res

def minion_game(string):
    s=string.lower()
    kevin=[]
    stuart=[]
    for i in range(len(s)):
        if s[i] in ['a','e','i','o','u']:
            kevin.append(s[i:])
        else:
            stuart.append(s[i:])

    kevin=length(kevin)
    stuart=length(stuart)

    res=[0,0]
    for word in set(kevin):
        count=0
        for i in range(len(s)):
            if s[i:i+len(word)]==word:
                count+=1
        res[0]+=count
    
    for word in set(stuart):
        count=0
        for i in range(len(s)):
            if s[i:i+len(word)]==word:
                count+=1
        res[1]+=count
        
    if res[0]==res[1]:
        print('Draw')
    elif max(res)==res[0]:
        print(f'Kevin {res[0]}')
    else:
        print(f'Stuart {res[1]}')

if __name__ == '__main__':
    s = input()
    minion_game(s)