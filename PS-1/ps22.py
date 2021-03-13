# PS-22 WAP to display following pattern
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *


for i in range(9,0,-1):
    for j in range(i):
        print("*",end="")
    print()
