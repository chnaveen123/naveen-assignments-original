def nozero(fnc):
    def helper(*args):

        print(fnc(*args))

    return helper


@nozero
def div(x, y):
    return x / y

@nozero
def mul(x, y):

    return x * y

@nozero
def add(x, y):

    return x + y

@nozero
def sub(x, y):

    return x - y

div(20,10)
add(20,10)
mul(10, 20)
sub(20, 10)
