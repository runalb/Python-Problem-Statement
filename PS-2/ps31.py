# PS-31 WAP to Swap the First and Last value of a list

def swap_first_n_last_val(li):
    first_val = li[0]
    last_val = li[-1]

    #adding last val to first pos
    li[0] = last_val
    #adding first val to last pos
    li[-1] = first_val

    return li


li = [0,1,2,3,4,5,6,7,8,9]

print("Before swap:\n",li)
print("After swap:\n",swap_first_n_last_val(li))


