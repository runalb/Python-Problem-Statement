# PS-36 WAP to remove the nth index character from a non-empty string

def remove_nth_idx_character(str,idx):
    c = 0
    res = ''

    for ch in str:
        c = c + 1
        if c == idx:
            pass
        else:
            res = res + ch
    return res



string = "Hello all"
print("Original String:\n",string)

idx = int(input(("\nEnter index to remove character: ")))

string = remove_nth_idx_character(string,idx)
print("\nString After removing {} idx character:\n {}".format(idx,string))




