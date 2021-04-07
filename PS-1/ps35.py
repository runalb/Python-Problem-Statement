# PS-35 Ask user to enter 10 element in the list and find even and odd from the list

def check_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

li=[]
li_len = 10
c=0

print("Enter 10 element to the list-")
while c != li_len:
    try:
        no = int(input("Enter element no.{} :".format(c+1)))
        li.append(no)
        c=c+1
    except:
        print("Invalid no! Enter integer no.")

print("Your list:\n",li)

li_even=[]
li_odd=[]

for n in li:
    if check_even(n):
        li_even.append(n)
    else:
        li_odd.append(n)

print("Even no:\n",li_even)
print("Odd no:\n",li_odd)
