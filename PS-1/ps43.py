# PS-43 WAP to accept two numbers from user and display all numbers between those numbers
'''
Ex- If user enters 3 and 9 program should display numbers 3,4,5,6,7,8,9
'''

no1 = int(input("Enter 1st no: "))
no2 = 0

while no2 < no1:
    print("2nd no. should be greater than 1st no.")
    no2 = int(input("Enter 2nd no: "))

for num in range(no1,no2+1):
    print(num,end=" ")