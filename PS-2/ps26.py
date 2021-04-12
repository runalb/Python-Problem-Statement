# PS-26 WAP to create a list of tuples with the first element as the number and second element as the square of the number

temp_li = []
li = []

user_input = ""
while user_input.upper() != "Y":
    print("Enter Integer no. OR To stop enter 'Y'")
    user_input = input("Enter no: ")
    try:
        temp_li.append(int(user_input))
        temp_li.append(int(user_input) * int(user_input))

        print("Tuple: {}\n".format(tuple(temp_li)))
        li.append(tuple(temp_li))

        temp_li = []

    except:
        print("Enter Integer no. OR To stop enter 'Y'\n")


print("List of Tuples:\n",li)