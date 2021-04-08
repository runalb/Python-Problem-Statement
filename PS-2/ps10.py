# PS-10 WAP to print odd numbers within a given range

try:
    print("Enter range -")
    start = int(input("Start: "))

    end = 0
    while end < start:
        print("End no. should be greater than start no.")
        end = int(input("End: "))

    print("\nOdd numbers in a range {} to {}:".format(start,end))
    for num in range(start,end+1):
        if num % 2 != 0:
            print(num,end=" ")

except:
    print("Invalid no!")