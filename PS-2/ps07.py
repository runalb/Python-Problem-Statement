# PS-07 WAP to print all numbers in a range divisible by a given number

try:
    print("Enter range-")
    start = int(input("Start: "))

    end = 0
    while end < start:
        print("End no. should be greater than start no.")
        end = int(input("End: "))

    no = int(input("Enter no: "))

    print("All numbers in a range {} to {} divisible by {}:".format(start,end,no))
    for x in range(start,end+1):
        if x % no == 0:
            print(x,end=" ")

except:
    print("Invalid no!")