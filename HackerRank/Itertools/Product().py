# Q : https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
from itertools import product as p

if '__main__'==__name__:
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    print(*list(p(a,b)))
    