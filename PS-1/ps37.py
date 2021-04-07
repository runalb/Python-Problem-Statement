# PS-37 Ask user to enter 10 element in the list and find all armstrong number from the list

def find_armstrong(num):
    res = 0
    no = num
    len_no = len(str(num))

    while (no != 0):
        d = no % 10
        res = res + d ** len_no
        no = no // 10

    if num == res:
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

print("Armstrong no:")
for no in li:
    if find_armstrong(no):
        print(no,end=" ")



