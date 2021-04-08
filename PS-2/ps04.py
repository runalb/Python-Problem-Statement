# PS-04 WAP to reverse a given number

no = int(input("Enter no: "))

org = no
rem = 0
rev = 0
while no > 0:
    rem = no % 10
    rev = rev * 10 +rem
    no = no//10

print("No:\n",org)
print("Reverse:\n",rev)
