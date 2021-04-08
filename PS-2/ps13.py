# PS-13 WAP find the count the number of digits in a number

try:
    no = int(input("Enter no: "))
    count = 0
    while no > 0:
        no = no//10
        count = count + 1
    print("Number of digits:",count)

except:
    print("Invalid value!")