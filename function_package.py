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



# 以自己封裝sikuli的函式為例===================================

def wrap(original_function, sleep_time):

    def new_function(*args, **kwargs):
        try:
            #執行原來的function
            original_function(*args, **kwargs)
        except:
            #如果找不到圖片, 做例外處理
            pass

    #命令執行完的等待時間
    sleep(sleep_time)
    return new_function



CLICK_SLEEP_TIME = 5
TYPE_SLEEP_TIME = 2
DRAG_DROP_SLEEP_TIME = 2

#套成新function
new_click = wrap(click, CLICK_SLEEP_TIME)
new_type = wrap(type, TYPE_SLEEP_TIME)
new_dragDrop = wrap(dragDrop, DRAG_DROP_SLEEP_TIME)


#以後若希望不拋出except, 就用下面指令
new_click("1441986043140.png")
new_click("1441986043140.png")
new_type("1441989903669.png", "123")
new_dragDrop("1441989997488.png", "1441989998610.png")




# 讓click不到, 再去catch exception做處理
# 與確認exist or not, 再去做click是不是一樣?

#=========================================================================


def check(original_function, sleep_time):

    def new_function(*args, **kwargs):
        execute = True
        if args[0][-4:] == ".png":
            execute = exists(args[0])

        if execute:
            try:
                original_function(*args, **kwargs)
            except:
                pass
        else:
            print "does not exist"

        sleep(sleep_time)

    return new_function


