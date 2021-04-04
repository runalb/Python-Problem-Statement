# PS-31 Take a list, say for example this one:
'''
a = [1,1,2,3,5,8,13,21,34,55,89]
and WAP that prints out all the elements of the list that are less than 5.

Extras-
1. Instead of printing the element one by one, make a new list that has all the element less than 5 from this list in it and print out ths new list
2. Ask the user for a number and return a list that contains only element from the original list a that are smaller than that number given by the user.
'''

a = [1,1,2,3,5,8,13,21,34,55,89]

li_less_than_5 = []
for x in a:
    if x<5:
        li_less_than_5.append(x)
print("New list- Element less than 5 \n",li_less_than_5)

no = int(input("Enter no:"))
li_less_than_user_no = []
for x in a:
    if x<no:
        li_less_than_user_no.append(x)
print("User list- Element less than user no from orignal list\n",li_less_than_user_no)
