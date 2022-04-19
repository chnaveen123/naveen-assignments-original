

from datetime import datetime

def logBeforeAfter(fun):

    def helper(*args, **kwargs):
        print(f"lon in before time : {datetime.now}")
        print(fun(*args))
        print(f"lon in after time : {datetime.now}")

    return helper


@logBeforeAfter
def fun(x, y):
    print("fun", x, y)

@logBeforeAfter
def fun1(*args):
    print("fun1", args)

@logBeforeAfter
def fun2(**kwargs):
    print("fun2", kwargs)

@logBeforeAfter
def fun3(*args, **kwargs):
    print("fun3", args, kwargs)


fun(2,3)
fun1(5,6)
fun2( first = "Chiruveru")
fun3(fun1,fun2)

