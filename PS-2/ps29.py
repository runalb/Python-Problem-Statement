# PS-29 WAP to generate random numbers from 1 to 20 and append them to the list

import random
li = []

user_input = int(input("Enter count: "))

for i in range(user_input):
    num = random.randrange(1,20)
    print("Random num generated:",num)
    li.append(num)

print("\nRandom num list:\n",li)
