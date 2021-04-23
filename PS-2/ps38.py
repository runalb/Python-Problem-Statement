# PS-38 WAP to form new string where the first character and the last character have been exchanged

def exchange_1st_n_last_ch(str):
    start = str[0]
    end = str[-1]

    exchange_string = end + str[1:-1] + start
    return exchange_string


string = "Hello all"
new_string = exchange_1st_n_last_ch(string)

print("Original string:\n",string)
print("New string after exchanging:\n",new_string)



