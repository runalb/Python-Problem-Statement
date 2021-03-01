# PS-14 WAP which will find all such no. which are divisible by 7 but are not a multiple of 5, between 2000 and 3200
# The numbers should be printed in a comma separated sequence on a single line

for x in range(2000,3200):
    if (x%7==0 and x%5!= 0):
        print(x,end=",")

