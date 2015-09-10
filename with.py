class Sample:
    def __enter__(self):
        return 5/2 == 2

    def __exit__(self, type, value, trace):
        print "type:", type
        print "value:", value
        print "trace:", trace
        #return True


def do_something():
    bar = 1 / 0



with Sample() as sample:
    if sample:
        do_something()

print "yy"
print "yy"
print "yy"
