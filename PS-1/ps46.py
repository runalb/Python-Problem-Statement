# PS-46 Modify above program to accept two numbers from user and display all numbers between them are divisible by 3

no1 = int(input("Enter 1st no: "))
no2 = 0

while no2 < no1:
    print("2nd no. should be greater than 1st no.")
    no2 = int(input("Enter 2nd no: "))

for num in range(no1,no2+1):
    if num % 3 == 0:
        print(num)