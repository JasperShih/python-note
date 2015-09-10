# -*- coding: utf8 -*-

def print_my_name(name):
    print "I am %s" % (name())


@print_my_name
def my_name():
    return "Hans"


"""
Step1:
excute print_my_name(my_name)

Step2:
my_name = the return value of Step1

#In this example, "print_my_name(my_name)"
didn't contain return statement, so it return
None to my_name. i.e. my_name = None

and now we cannot call my_name(That's because it is None.
It's not the function anymore)
"""

u"""
如果要讓 my_name 可以被 call，只要加一行 return function 就可以了，如下例。
def print_my_name(name):
    print “I am %s” %(name())
    return name # return 傳進來的 function

@print_my_name
def my_name():
    return “Hans”
這樣 my_name 就又可以被 call 了。

說穿了 decorator 就是個便利寫程式的語法糖。

class也可以用, 可以看成正常語法的省略版
"""


"""
示意圖


@print_my_name
         ^
        ^  v
       ^    v
#start^      v
     ^        v
def my_name():
    return "Hans"


"""