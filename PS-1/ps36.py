# PS-36 Ask user to enter 10 element in the list and find prime number from the list

def check_prime_no(n):
    temp = n // 2
    if (n > 1):
        for x in range(2, temp + 1):
            if (n % x == 0):
                return False
                break
        else:
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

li_prime=[]
for n in li:
    if check_prime_no(n):
        li_prime.append(n)
print("Prime no:\n",li_prime)

