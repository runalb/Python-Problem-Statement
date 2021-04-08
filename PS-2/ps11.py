# PS-11 WAP find the sum of digits in a number

try:
    no = int(input("Enter no: "))
    sum = 0
    while no > 0:
        rem = no % 10
        sum = sum + rem
        no = no//10
    print("Sum of digits:",sum)

except:
    print("Invalid value!")