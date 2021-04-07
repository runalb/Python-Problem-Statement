# PS-39
'''
With a given integral number n, WAP to generate a dictionary that contains (i,i*i) such that is an integral between 1 and n (both included) and then the program should print the the dictionary
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64}
'''

dict1 = {}

try:
    n = int(input("Enter integral no: "))

except:
    print("Invalid value")

for i in range(1,n+1):
    v = i * i
    dict1[i] = v

print(dict1)
