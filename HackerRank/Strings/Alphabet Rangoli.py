import string
def print_rangoli(size):
    alphabets=list(string.ascii_lowercase)
    out=[alphabets[size-1]]

    s=alphabets[size-1]
    for i in range(size-1):
        out.append(s+'-'+alphabets[size-i-2]+'-'+s[::-1])
        s+='-'+alphabets[size-i-2]
        
    for i in range(1,(size*2)):
        if i>size:
            i=(size*2)-i
        print(out[i-1].center((size*4)-3,'-'))

    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)