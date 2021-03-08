# PS-25 WAP to display following pattern
'''
111111111
22222222
3333333
444444
55555
6666
777
88
9
88
777
6666
55555
444444
3333333
22222222
111111111
'''



no = 1
for i in range(9,0,-1):
    for j in range(i):
        print(no,end="")
    #incerement no
    no = no + 1
    print()


if no > 9 :
    for i in range(1,10,1):
        # decrement no
        no = no - 1
        if i == 1:
            continue
        for j in range(i):
            print(no, end="")
        print()