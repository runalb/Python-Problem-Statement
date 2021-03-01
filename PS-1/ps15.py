# PS-15 WAP which can compute the factorial of given number

n = int(input("Enter no: "))
f = 1

for x in range(1,n+1):
    f = f * x

print("Factorial of {} is {}".format(n,f))