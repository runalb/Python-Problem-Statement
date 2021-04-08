# PS-44 Modify above program to accept two numbers and display table of numbers between them.
# Note: If user enters 3 and 7. Display table of 4,5 and 6

no1 = int(input("Enter 1st no: "))
no2 = 0

while no2 < no1:
    print("2nd no. should be greater than 1st no.")
    no2 = int(input("Enter 2nd no: "))

for num in range(no1+1,no2):
    print("Table of",num)
    for x in range(1,10+1):
        print("{} x {} = {}".format(num,x,num*x))
    print()
