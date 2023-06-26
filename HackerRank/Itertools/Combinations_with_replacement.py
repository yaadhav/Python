# Q : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
from itertools import combinations_with_replacement as c

if '__main__'==__name__:
    a=input().split()

    for item in list(c(sorted(a[0]),int(a[1]))):
        print(''.join(item))
    