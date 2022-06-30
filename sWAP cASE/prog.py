def swap_case(s):
    s1 = ''
    for i in s:
        if i.islower():
            s1 = s1 + i.upper()
        else:
            s1 = s1 + i.lower()
        
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)