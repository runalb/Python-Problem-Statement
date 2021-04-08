# PS-47 WAP to accept 10 numbers and display in ascending and descending order

counter = 0
li = []

print("Enter 10 numbers one by one-")
while counter != 10:
    try:
        no = int(input("Enter no {}: ".format(counter+1)))
        li.append(no)
        counter = counter + 1
    except:
        print("Invalid value!\n")

li.sort()
print("Ascending order:\n",li)

li.sort(reverse=True)
print("Desending order:\n",li)


