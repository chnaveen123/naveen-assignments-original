num = 2
counter = 1


for i in range(4):
    for j in range(1, num):
        if counter == 10:
            counter = 0
        print(counter, end=' ')
        counter += 1
    print("")
    num += 1