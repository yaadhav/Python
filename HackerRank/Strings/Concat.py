def count_substring(string, sub_string):

    sub_len=len(sub_string)
    str_len=len(string)

    ans=0
    for ind in range(0, str_len-sub_len+1):
        if string[ind:ind+sub_len]==sub_string:
            ans+=1
    return ans

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)