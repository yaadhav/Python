# Q : https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
from itertools import combinations as c

if '__main__'==__name__: 
    a=input().split()

    for k in range(1,int(a[1])+1):
        for item in list(c(sorted(a[0]),k)):
            print(''.join(item))
    