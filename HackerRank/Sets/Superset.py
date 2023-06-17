# Q : https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

if __name__=='__main__':
    a=set(map(int, input().split()))

    check=True
    for _ in range(int(input())):
        b=set(map(int, input().split()))

        if not b.issubset(a) or len(a)<=len(b):
            check=False

    print(check)