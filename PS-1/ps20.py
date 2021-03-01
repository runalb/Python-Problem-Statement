# PS-20 Modify previous program (PS-19) to accept a number between 1 to 9 from  user and display pattern accordingly
# ex -
#  1
#  22
#  333
#  4444

len = int(input("Enter no. between 1 to 9: "))

if len>1 and len<9:

    for num in range(1,len+1):
        for row in range(num):
            print(num,end="")
        print()

else:
    print("Invalid no.! Please enter no. between 1 to 9")
