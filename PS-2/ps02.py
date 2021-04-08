# PS-02 WAP to exchange the values of two numbers without using a temporary variable

n1 = 10
n2 = 6

print("Before exchange:")
print("n1={} n2={}".format(n1,n2))

#exchangng the values of two numbers without using a temporary variable
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2

print("After exchange:")
print("n1={} n2={}".format(n1,n2))
