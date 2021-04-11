# PS-25 WAP to find the union of two list

l1 = [1,342,3546,44,1,542,7867,54,234,3,55,66,89,44]
l2 = [5,6,745,2,541,1,65,88,34,66,44,66,88]
union_li = []

for element in l1:
    if element not in union_li:
        union_li.append(element)

for element in l2:
    if element not in union_li:
        union_li.append(element)

print("Union List:\n",union_li)
