# Q : https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

def Counter(mylist):
    count={}
    for item in mylist:
        if item not in count:
            count[item]=0
        count[item]+=1
        
    return count

if __name__=='__main__':
    k=int(input())
    rooms=list(map(int,input().split()))

    count=Counter(rooms)
    for keys in count.keys():
        if count[keys]==1:
            print(keys)
