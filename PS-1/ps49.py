# PS-49 WAP to accept a string and display whether it is a palindrome

def check_palindrome_str(str):
    s1 = ''
    for ch in str:
        s1 = ch + s1

    if s1 == str:
        return True
    else:
        return False

str = input("Enter string: ")

if check_palindrome_str(str):
    print(str,"is Palindrome string")
else:
    print(str,"is not a Palindrome string")

