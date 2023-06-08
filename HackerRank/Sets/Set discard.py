# Q: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

if __name__ == '__main__':
    n=int(input())
    a=set(map(int,input().split()))
    m=int(input())

    for _ in range(m):
        s=input().split()

        if s[0]=='pop':
            a.discard(list(a)[0])
        elif s[0]=='discard':
            a.discard(int(s[1]))
        else:
            try:
                a.remove(int(s[1]))
            except:
                pass
        print(a)
    
    print(sum(a))
        