# PS-21 WAP to display following pattern

# 11111111
# 2222222
# 333333
# 44444
# 5555
# 666
# 77
# 88
# 9


no = 1
for i in range(9,0,-1):
    for j in range(0,i):
        print(no,end="")
        
    #incerement no
    no = no + 1
    print()