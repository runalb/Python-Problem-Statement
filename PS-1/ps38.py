# PS-38 WAP to create 3 list and restrict the user to insert only prime number in first_list, only palindrom number in second_list, only Armstrong number in third_list


#prime no. list
first_li=[]

#palindrome no. list
second_li=[]

#armstrong no. list
third_li=[]

def check_prime_no(no):
    temp = no // 2
    if (no > 1):
        for x in range(2, temp + 1):
            if (no % x == 0):
                return False
                break
        else:
            return True
    else:
        return False


def check_palindrom(no):
    rem = 0
    rev = 0
    org = no
    while (no > 0):
        rem = no % 10
        rev = rev * 10 + rem
        no = no // 10

    if (org == rev):
        return True
    else:
        return False


def check_armstrong(num):
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



user_ans = ''
while user_ans.upper() != 'N':
    try:
        no = int(input("Enter your no.:"))

        if check_prime_no(no):
            first_li.append(no)
            print(no,"added to first list")

        if check_palindrom(no):
            second_li.append(no)
            print(no,"added to second list")

        if check_armstrong(no):
            third_li.append(no)
            print(no,"added to third list")

        user_ans= input("\nAdd more element? Type 'N' to stop: ")

    except:
        print("Invalid Input!")


print("First list stores - Prime no.\n",first_li)
print("Second list stores - Palindrome no.\n",second_li)
print("Third list stores - Armstrong no.\n",third_li)
