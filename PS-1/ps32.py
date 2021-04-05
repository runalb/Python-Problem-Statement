# PS-32 Ask the user for a string and print out whether this is palindrome or not.(A palindrome is a string that reads the same forwards and backwards)

print("Check the string is palindrome or not")
str = input("Enter your string: ")

rev_str = ""
for x in str:
    rev_str = x + rev_str

if rev_str == str:
    print("{} is palindrome".format(str))
else:
    print("{} is not a palindrome".format(str))