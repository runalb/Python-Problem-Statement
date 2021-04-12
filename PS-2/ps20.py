# PS-20 WAP to put Even and Odd element in a list into two different lists

def check_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

even_li = []
odd_li = []

user_input = ""
while user_input.upper() != "Y":
    print("Enter Integer no. OR To stop enter 'Y'")
    user_input = input("Enter no: ")
    try:
        if check_even(int(user_input)):
            even_li.append(int(user_input))
            print("{} Added to Even List\n".format(user_input))
        else:
            odd_li.append(int(user_input))
            print("{} Added to Odd List\n".format(user_input))

    except:
        print("Enter Integer no. OR To stop enter 'Y'\n")


print("Even list\n",even_li)
print("Odd list\n",odd_li)
