# PS-24 WAP to display following pattern
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********


for i in range(1,9+1):
    for j in range(i):
        print("*",end="")
    print()
