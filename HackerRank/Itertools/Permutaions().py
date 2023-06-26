# Q : https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
from itertools import permutations as p

if '__main__'==__name__:
    a=input().split()

    for item in sorted(list(p(a[0],int(a[1])))):
        print(''.join(item))
    