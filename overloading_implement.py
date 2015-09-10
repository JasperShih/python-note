__author__ = 'Jasper'

type("d")
type("d", Key.WIN)
type("1441889288761.png", "d")
type("1441889288761.png", "d", Key.WIN)


# SOL1
def func1(a, b, c):
    pass


def func2(a, b):
    pass


def func3(a, b=None):
    pass


def func(a, b, c=None):
    if c:
        func1(a, b, c)
    elif type(b) == "string":
        func2(a, b)
    else:
        func3(a, b)


# SOL2
def add_bullet(self, **kwargs):
    pass
