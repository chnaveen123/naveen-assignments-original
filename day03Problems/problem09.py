A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = sum(A)
print(f"sum : {sum}")

print("*" * 40)

sum = 0
for i in A:
    sum += i
    print(f"sum : {sum}")