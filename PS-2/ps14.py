# PS-14 WAP to check if a number is a Palindrome
try:
    no = int(input("Enter no: "))

    org = no
    rem = 0
    rev = 0
    while no > 0:
        rem = no % 10
        rev = rev * 10 + rem
        no = no//10

    if rev == org:
        print(org,"is Palindrome")
    else:
        print(org,"is not a Palindrome")

except:
    print("Invalid value!")