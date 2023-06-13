# Q : https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

if __name__=='__main__':
    
    for _ in range(int(input())):
        input()
        a=list(map(int,input().split()))
        input()
        b=list(map(int,input().split()))

        ans=True
        for num in a:
            if num in b:
                b.remove(num)
            elif num not in b:
                ans=False 

        print(ans)
