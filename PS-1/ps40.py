# PS-40 WAP which accepts a sequence of comma-separated numbers from the console and generate a list and a tuple which contains every number
'''
Suppose the following input is supplied to the program
34,67,55,33,12,98
Then the output should be:
['34','67','55','33','12','98']
('34','67','55','33','12','98')
'''

user_input = input("Enter comma-separated no.:\n")

num_li = user_input.split(',')
print("list:\n",num_li)

num_tuple = tuple(num_li)
print("Tuple:\n",num_tuple)