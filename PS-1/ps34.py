# PS-34 WAP to replace minimum element from the list by "maximum element+1" and display the result.
'''
For ex-
Input:  L=[22,56,365,989,356]
Output: L=[990,56,365,989,356]
'''

li = [22,56,365,989,356]

print("Input:  L=",li)

max = li[0]
min = li[0]

for no in li:
    if no > max:
        max = no
    elif no < min:
        min = no

c=0
for x in li:
    if x == min:
        c_min = c
        c = c + 1
    else:
        c = c + 1

li.pop(c_min)
li.insert(c_min,max+1)
print("Output: L=",li)


