list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,9]
common_elements = set(list1).intersection(set(list2))
print(common_elements)

print("*" * 40)


list3 = []
for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)
print(list3)