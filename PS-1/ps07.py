# PS-07 WAP to accept two numbers and one of the following operators +, -, *, /. Perform the given operation and display result

n1 = float(input("Enter 1st no. : "))
n2 = float(input("Enter 2nd no. : "))

op = str(input("Enter any one operator to perform operation \n(+, -, *, /) \n"))

if op == "+":
    res = n1 + n2
    print("Add:", res)

elif op == "-":
    res = n1 - n2
    print("sub:", res)

elif op == "*":
    res = n1 * n2
    print("mul:", res)

elif op == "/":
    res = n1 / n2
    print("div:", res)

else:
    print("invalid operator - try again!")

