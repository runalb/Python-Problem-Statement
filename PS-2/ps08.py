# PS-08 WAP to read two numbers and print their Quotient and Remainder

try:
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))
except:
    print("Invalid value!")

rem = no1%no2
print("Remainder:",rem)

quo = no1//no2
print("Quotient:",quo)