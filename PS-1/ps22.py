# PS-21 WAP to display following pattern
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
    for j in range(0,i):
        print("*",end="")
    print()
