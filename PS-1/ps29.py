# PS-29 WAP to display 10 numbers that are divisible by 5 and 7

num = 1
count = 0

while count != 10:
    if ( (num % 5 == 0) and (num % 7 == 0) ):
        print(num)
        count = count + 1
        num = num + 1

    else:
        num = num + 1
