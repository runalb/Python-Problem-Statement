# PS-11 WAP to check weather user inputted number is palindrome or not

no=int(input("Enter No: "))

rem=0
rev=0
org=no
while(no>0):
    rem=no%10
    rev=rev*10+rem
    no=no//10

if(org==rev):
        print("palindrome")
else:
    print("not palindrome")
