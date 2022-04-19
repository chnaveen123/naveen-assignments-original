d1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_presented(x):
    if x in d1:
        print("key presented")
    else:
        print("Not presented")

is_presented(2)
is_presented(8)

