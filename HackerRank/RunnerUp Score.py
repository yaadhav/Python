if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr=sorted(arr)

    ind=-2
    while arr[ind]==arr[-1]:
        ind-=1

    print(arr[ind])

