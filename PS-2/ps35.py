# PS-35 WAP to replace all occurrences of 'a' with $ in a string

def replace_string_with(str,ch1,ch2):
    res = ''
    for ch in str:
        if ch == ch1:
            res = res + ch2
        else:
            res = res + ch
    return res

user_input = input("Enter string: ")
print(user_input)

user_input = replace_string_with(user_input,'a','$')
print(user_input)


