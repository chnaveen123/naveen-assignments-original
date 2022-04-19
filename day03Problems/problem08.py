l = [0, 1, 0,2,3, 0, 1,0, 0,6, 1, 1]
val = 0

try:
    while True:
        l.remove(val)
except ValueError:
    pass

print(l)