# Q: https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

def happiness(array,a,b):
    result=0
    for num in array:
        if num in a:
            result+=1
        elif num in b:
            result-=1
    return result

if __name__ == '__main__':
    input()
    array = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = happiness(array,a,b)
    print(result)