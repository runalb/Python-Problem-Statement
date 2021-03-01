# PS-16 WAP to test whether a passed letter is a vowel or not

str = input("Enter String: ")
vowel = "AEIOUaeiou"

#loop x through str to get each ch in variable x
for x in str:
    #check if x is present in vowel
    if x in vowel:
        #if x is vowel
        print(x, "is vowel")


    #else x is not a vowel
    else:
        print(x, "is not a vowel")
