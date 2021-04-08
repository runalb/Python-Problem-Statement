# PS-15 WAP to print all integers that aren't divisible by either 2 or 3 and lie between 1 to 50

for num in range(1,50+1):
    if (num % 2 != 0) and (num % 3 != 0):
        print(num,end=" ")
