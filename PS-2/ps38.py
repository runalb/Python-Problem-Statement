# PS-38 WAP to form new string where the first character and the last character have been exchanged

def exchange_1st_n_last_ch(str):
    str_li = []
    for ch in str:
        str_li.append(ch)

    # exchanging 1st ch to last ch
    first_ele = str_li[0]
    last_ele = str_li[-1]

    str_li[0] = last_ele
    str_li[-1] = first_ele

    res = ''
    for ch in str_li:
        res = res + ch
    return res


string = "Hello all"
print("Original string:\n",string)

string = exchange_1st_n_last_ch(string)
print("string after exchanging:\n",string)



