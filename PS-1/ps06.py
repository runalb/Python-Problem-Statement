# PS-06 WAP to accept 3 numbers and display smallest and largest number

num_l = []
for x in range(3):
    no = float(input("Enter no. :"))
    num_l.append(no)

print(num_l)

#using min max function
print("= Using min, max function =")
print("Smallest",min(num_l))
print("largest",max(num_l))



#2nd soln-
print("\n\n====== 2nd soln ======")

largest = None
smallest = None
for x in range(3):
    num = float(input("Enter a number: "))
    try:
        if largest is None:
            largest = num
        if smallest is None:
            smallest = num
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    except:
        print ("Invalid input")

print ("Minimum is", smallest)
print ("largest is", largest)
