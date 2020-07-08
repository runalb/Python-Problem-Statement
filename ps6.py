no=input("Enter no: ")
for x in range(9,-1,-1):
    temp=str(x)
    if(temp in no):
        print("Large: ",temp)
        break
for x in range(10):
    temp=str(x)
    if(temp in no):
        print("small: ",temp)
        break