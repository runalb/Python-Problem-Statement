# PS-32 WAP to remove the duplicate items from a list

def remove_duplicate(li):
    res_li = []
    for num in li:
        if num not in res_li:
            res_li.append(num)
    return res_li


li = [1,2,3,4,5,6,7,8,9,1,2,3]

print("Original List:\n",li)

li = remove_duplicate(li)
print("\nRemoved duplicate items form the list:\n",li)


