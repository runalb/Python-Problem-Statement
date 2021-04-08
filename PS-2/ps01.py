# PS-01 WAP to calculate the average of numbers in a given list

li = [45,453,34,23,56,323,53,553]

total = 0
for num in li:
    total = total + num

avg = total/(len(li))

print("List:\n",li)
print("Average:\n",avg)
