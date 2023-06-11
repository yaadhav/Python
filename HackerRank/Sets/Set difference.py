# Q: https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

if __name__ == '__main__':
    input()
    s1=set(map(int,input().split()))
    input()
    s2=set(map(int,input().split()))

    s=s1.difference(s2)
    print(len(s))