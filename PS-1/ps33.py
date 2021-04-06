# PS-33 Ask user to enter 10 elements in the list and find minimum and maximum of from the list

try:
    li_len = int(input("Enter length of list: "))
except:
    print("Invalid no.! Please enter integer")

li=[]
counter = 0
while counter != li_len:
    try:
        n = int(input("Enter No: "))
        li.append(n)
        counter = counter + 1
    except:
        print("Please enter integer no")

print("Your list:\n",li)

max = li[0]
min = li[0]
for no in li:
    if no > max:
        max = no
    elif no < min:
        min = no

print("Max no. in the list: {}".format(max))
print("Min no. in the list: {}".format(min))



