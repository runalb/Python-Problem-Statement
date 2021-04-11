# PS-17 WAP to read a number n and print the natural numbers summation pattern
'''
ex-
Input: 5
Output:
1 = 1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
1 + 2 + 3 + 4 + 5 = 15
'''

n = int(input("Enter no"))

sum = 0
for x in range(1,n+1):
    for num in range(1,x+1):
        print(num,end="")
        sum = sum + num
        if num == x:
            print(" = {}".format(sum))
        else:
            print(" + ",end="")
    sum = 0

