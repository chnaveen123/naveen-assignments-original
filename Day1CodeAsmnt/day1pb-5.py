

cntr = 0
j = 1
while cntr < 6:
    num = j
    flag = False
    lst = []
    for i in range(3):
        if (num - 1) % 3 == 0:
            res = (num - 1) // 3 + 1
            lst.append(res)
            num = num - res
            if i == 2:
                flag = True
        else:
            break
    if flag and num and num % 3 == 0:
        print("Total {} -->  remaining {} --> father distributes {} to each daughter".format(j, num, num//3))
        print("\t\tDaughter #1 --> {}\n\t\tDaughter #2 -->{}\n\t\tDaughter #3 --> {}".format(lst[0], lst[1], lst[2]))
        cntr += 1
    j += 1