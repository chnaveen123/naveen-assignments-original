d1 = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20, 'F': 15}

temp = []
result = dict()
for key, value in d1.items():
    if value not in temp:
        temp.append(value)
        result[key] = value
print(result)


