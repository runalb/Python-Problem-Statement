# PS-48 WAP to accept string from user and a single character. Display how many times given characters occurs in a given a given string

def count_single_character_in_string(str,ch):
    counter = 0
    for c in str:
        if c == ch:
            counter = counter + 1
    return counter

str = input("Enter your string: ")
ch=''
while len(ch) != 1:
    ch = input("Enter single character: ")

print("\nYour string:\n",str)
print("No. of times '{}' occurs in string:\n".format(ch),count_single_character_in_string(str,ch))


