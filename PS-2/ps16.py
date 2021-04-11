# PS-16 WAP to read a number n and print the series "1+2+.....+n="

n = int(input("Enter no: "))
sum = 0
for num in range(1,n+1):
    print(num,end="")
    sum = sum + num

    if num == n:
        print("={}".format(sum),end="")
    else:
        print("+",end="")