# Q: https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-sets
if __name__ == '__main__':
    input()
    s1=set(map(int,input().split()))

    for _ in range(int(input())):
        a=input().split()
        s2=set(map(int,input().split()))

        if a[0]=='intersection_update':
            s1.intersection_update(s2)
        elif a[0]=='update':
            s1.update(s2)
        elif a[0]=='symmetric_difference_update':
            s1.symmetric_difference_update(s2)
        elif a[0]=='difference_update':
            s1.difference_update(s2)

    print(sum(s1))
        