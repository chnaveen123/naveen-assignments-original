"""def func(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
        return f
n = input()
m = str(n)
length = len(m)
sum = 0
for i in m:
    sum = sum + func(int(i))
if sum == n:
    print("Strong Number")
else:
    print("Not a strong number")
"""


factorial = [1, 1, 2, 6, 24, 120,
             720, 5040, 40320, 362880]


def isStrong(N):

    num = str(N)

    sum = 0

    for i in range(len(num)):
        sum += factorial[ord(num[i]) -
                         ord('0')]


    if sum == N:
        return True
    else:
        return False



def printStrongNumbers(N):

    for i in range(1, N + 1):

        if (isStrong(i)):
            print(i, end=" ")



if __name__ == "__main__":

    N = 2000


    printStrongNumbers(N)


