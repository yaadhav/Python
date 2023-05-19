if __name__ == '__main__':
    n,m=input().split()
    n,m=int(n),int(m)
    pattern=[]

    for i in range(int(n/2)):
        string='.|.'*((2*i)+1)
        pattern.append(string)

    for i in range(n):
        if i<int(n/2):
            print(pattern[i].center(m,'-'))
        elif i==int(n/2):
            print('WELCOME'.center(m,'-'))
        else:
            print(pattern[n-i-1].center(m,'-'))
