# -*- coding: utf8 -*-

__author__ = 'Jasper'


def show(a, b, c, d):
    print a + b + c +d


def new_type(*args, **kwargs):
    # Set up
    print "in"


    args = args + ('yo', 'cc')

    show(*args,  **kwargs)

    # Tear down

    print "out"


#======================================


def new_type(func, sleep_time):
    def tmp(*args, **kwargs):
        # Set up
        print "in"

        # Execute and try except
        try:
            func(*args, **kwargs)
        except:
            pass

        # Tear down (Can be try catch)
        print "out"
        sleep(sleep_time)

    return tmp


#@new_type
def show(a, b):
    print a + b



new_show = new_type(show, 5)


#===================================


# context的參數, 及裡面function的參數如何傳遞
class context:
    def __init__(self, may_png, sleep_time):
        self.may_png = may_png
        self.sleep_time = sleep_time

    def __enter__(self):

        found = True
        if self.may_png[-3:] == "png":
            pass
            # found = chaeck the png exist or not

        return found

    def __exit__(self, type, value, trace):
        print "type:", type
        print "value:", value
        print "trace:", trace
        # return True
        # or return isinstance(value, TypeError)

        sleep(self.sleep_time)


def checker(func):
    def tmp(*args, **kwargs):
        sleep_time = args[-1]
        with context(args[0], sleep_time) as found:
            if found:
                func(*args[:-1], **kwargs)
    return tmp


check_click = checker(click)

check_click(5)