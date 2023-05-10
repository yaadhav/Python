if __name__ == '__main__':
    N = int(input())
    ans=[]
    
    for _ in range(N):
        s=input().split()

        if s[0]=='insert':
            ans.insert(s[2],s[1])
        if s[0]=='print':
            print(ans)
        if s[0]=='sort':
            ans=sorted(ans)
        if s[0]=='append':
            ans.append(s[1])
        if s[0]=='pop':
            ans.pop()
        if s[0]=='reverse':
            ans=ans[::-1]