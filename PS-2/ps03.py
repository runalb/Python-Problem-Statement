# PS-03 WAP to read a number n and compute n+nn+nn

no = int(input("Enter no: "))

temp = str(no)
t1 = temp + temp
t2 = temp + temp + temp

print("{} + {} + {} =".format(no,t1,t2))
res = no + int(t1) + int(t2)
print(res)
