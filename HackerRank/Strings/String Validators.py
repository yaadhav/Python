if __name__ == '__main__':
    s = input()
    results=[False,False,False,False,False]

    for letter in s:
        if letter.isalnum():
            results[0]=True
        if letter.isalpha():
            results[1]=True
        if letter.isdigit():
            results[2]=True
        if letter.islower():
            results[3]=True
        if letter.isupper():
            results[4]=True

    for result in results:
        print(result)
    
