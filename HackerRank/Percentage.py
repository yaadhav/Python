if __name__ == '__main__':

    d={}    
    for _ in range(int(input())):
        s=input().split()
        d[s[0]]=(float(s[1])+float(s[2])+float(s[3]))/3
    key=input()

    print("{0:.2f}".format(d[key]))


