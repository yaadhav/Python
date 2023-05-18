def wrap(string, max_width):
    
    result=''
    for i in range(len(string)):
        result+=string[i]
      
        if i%max_width==max_width-1 or i==len(string)-1:
            result+='\n'

    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)