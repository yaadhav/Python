# Q: https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

def symmetric_difference(m,n):
    diff1=m.difference(n)
    diff2=n.difference(m)
    result=diff1.union(diff2)    
    return sorted(result)

if __name__ == '__main__':
    input()
    m = set(map(int, input().split()))
    input()
    n = set(map(int, input().split()))
    result = symmetric_difference(m,n)
    for num in result:
        print(num)