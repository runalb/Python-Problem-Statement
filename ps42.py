no=int(input("Enter value: "))
c500=c100=c50=c20=c10=c5=c2=c1=0
while(no>0):
    if(no>=500):
        c500=c500+1
        no=no-500
    elif(no>=100):
        c100=c100+1
        no=no-100
    elif (no >= 50):
        c50 = c50 + 1
        no = no - 50
    elif (no >= 20):
        c20 = c20 + 1
        no = no -20
    elif (no >= 10):
        c10 = c10 + 1
        no = no - 10
    elif (no >= 5):
        c5 = c5 + 1
        no = no - 5
    elif (no >= 2):
        c2 = c2 + 1
        no = no - 2
    else:
        c1=c1+1
        no = no - 1
print("500:",c500)
print("100:",c100)
print("50:",c50)
print("20:",c20)
print("10:",c10)
print("5:",c5)
print("2:",c2)
print("1:",c1)
