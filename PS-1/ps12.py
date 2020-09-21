# PS-12 WAP to check weather user inputted number is prime or not

num = int(input("Enter no: "))

#divide no by 2 and get nearest whole no. and stored in temp
temp=num//2

# If given number is greater than 1.
if (num>1):

    #range 2 to temp ie- 2,3,..... upto temp
    for x in range(2,temp+1):

        #If no is divisible by any number between 2 to n / 2 ie. temp.
        #it is not prime if reminder = 0
        if(num % x == 0):
            print(num,"is not prime no.")
            break

    else:
        print(num,"is prime no.")

#bcs prime no. starts from 2 else it not a prime
else:
    print(num,"is not prime no.")

