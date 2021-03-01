# PS-18 WAP to accept two numbers from user and display all numbers between those numbers
# ex- if user enters 3 and 9 program should display 3,4,5,7,8 and 9

start = int(input("Enter no: "))
end = int(input("Enter no: "))

for x in range(start,end+1):
    print(x,end=" ")
