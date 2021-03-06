# PS-12 WAP to check weather user inputted number is Armstrong or not

num = int(input("Enter no: "))

res = 0
no = num
len_no = len(str(num))

while(no!=0):
    d = no%10
    res = res + d ** len_no
    no = no//10

if num == res:
    print(num,"is a Armstrong Number ")
else:
    print(num,"is not a Armstrong Number ")