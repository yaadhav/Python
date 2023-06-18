# Q : https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
import math as m

ab,bc=int(input()),int(input())

bcm=m.atan(ab/bc)*180/m.pi
print(f'{round(bcm)}{chr(176)}')