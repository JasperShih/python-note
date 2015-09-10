class Sample:
    def __init__(self):
        pass

    def __enter__(self):
        return 5 / 2 == 2

    def __exit__(self, type, value, trace):
        print "type:", type
        print "value:", value
        print "trace:", trace
        # return True
        # or return isinstance(value, TypeError)


def do_something():
    bar = 1 / 0


with Sample() as sample:
    if sample:
        do_something()

print "yy"
print "yy"
print "yy"

""" deal in exception in __exit__
or like that:

try:
    with open( "a.txt" ) as f :
        do something
except xxxError:
    do something about exception

or

try:
    with open( "a.txt" ) as f :
        do something
        .
        .
    .
    .
    .
    .
    .
except xxxError:
    do something about exception

    """

