l=[1,2,3,4,5,6,7,8,9]
l1=[]
lC=[]

print(l)
for x in l:
    status=0
    temp=x//2
    for y in range(2,temp+1):
        if(x%y==0):
            status=1
    if(status==0):
        l1.append(x)
    else:
        lC.append(x)
print("Prime List :\n",l1)
print(lC)

l2=[]
for y in l:
    rev=0
    org=0
    rem=0
    while(y>0):
        rem=y%10
        rev=rev*10+rem
        y=y//10
        if(rev==org):
            l2.append(y)