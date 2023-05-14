def swap_case(s):
    
    res=''
    for letter in s:
        if letter==letter.lower():
            res+=letter.upper()
        elif letter==letter.upper():
            res+=letter.lower()
        else:
            res+=letter
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)