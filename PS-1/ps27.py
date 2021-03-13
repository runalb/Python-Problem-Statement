# PS-27 WAP to accept numbers and display its table.
'''
Note: If user enters 7 output should be as follows
7 x 1 = 7
7 x 1 = 14
...
...
7 x 1 = 70
'''


num = int(input("Enter no: "))

for x in range(1,10+1):
    res = num * x
    print("{} x {} = {}".format(num, x, res))