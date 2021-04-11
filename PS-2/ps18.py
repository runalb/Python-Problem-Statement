# PS-18 WAP to print an Identity Matrix
'''
ex-
Enter no: 4
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
'''

no = int(input("Enter no: "))

for i in range(0,no):
    for j in range(0,no):
        if i == j:
            print(" {} ".format(1),end="")
        else:
            print(" {} ".format(0),end="")

    print()