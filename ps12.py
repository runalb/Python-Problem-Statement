#prime or not

no=int(input("Enter value: "))
status=0
temp=no//2
for x in range(2,temp+1):
    if(no%x==0):
        status=1
if (status==1):
    print("Not Prime")
else:
    print("Prime")