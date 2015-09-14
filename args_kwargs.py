# -*- coding: utf8 -*-
__author__ = 'Jasper'

"""
*var : unpack完之後的var等於傳進來的arg1, arg2...(key=value sequence除外)
所以var(未unpack) = (arg1, arg2...)  #只會加tuple的外框
**var :unpack完之後的var等於傳進來的key1 = value1, key2 = value2... sequence
所以var(未unpack) = {key1 = value1, key2 = value2...}



*args, **kwargs中的args, kwargs就只是一般的引數名稱, 這些名子是可以改的
用args (arguments), kwargs (keyword arguments)只不過是約定俗成的用法

"""
def show(*args, **kwargs):
    print args
    print kwargs


"""
eg:
show(1,2,3,k=1,g=2)
=>
(1, 2, 3)
{'k': 1, 'g': 2}
"""


def display(a, b, c, d, e):
    print a
    print b
    print c
    print d
    print e


tuple_a = (1, 2, 3, 4, 5)  # 1
list_a = [1, 2, 3, 4, 5]  # 2
set_a = {1, 2, 3, 4, 5}  # 3

dict_a = {'a': 123456,  # 4
          'b': 321,
          'c': 9526,
          'd': 7755,
          'e': 488}

dict_b = {'f': 123456,
          'j': 321,
          'k': 9526,
          'l': 7755,
          'm': 488}

"""
在function call的arguments中, *是unpacking sign,將一個*加在python的data structure前,
則會將其data structure解開, 並將裡面的各個element傳到callee去.

如
show(tuple_a) = show((1,2,3,4,5))
show(list_a) = show([1,2,3,4,5])
show(set_a) = show({1,2,3,4,5})

而
show(*tuple_a)和show(*list_a)和show(*set_a)
= show(1,2,3,4,5)

字典則是
show(dict_a) = show(
         {'a': 123456,  # 4
          'b': 321,
          'c': 9526,
          'd': 7755,
          'e': 488})
和
show(*dict_a) = show('c','a', 'b', 'e', 'd') 注意是亂序的, 因為字典並沒有順序
show(**dict_a) = show(a = 123456, e = 488, b = 321, d=7755, c = 9526) 也是亂序傳出

注意
display(dict_b)會報錯, 因為這等於
display(f = 123456, j = 321, k = 9526, l = 7755, m = 488)
而display並沒有對應接收的參數

display(**dict_a) 就會正確了


*號表示將data structure解開的意思(其elements傳出是有序的);
dict 比較特別, *解開並只傳出key值(其elements傳出是亂序的),
**才是傳出各elements, i.e. key1:value1, key2:value2 ......(也是亂序),
*號可視為把data structure外面那一層框拔掉的意思


show(1,2,3,4,5)
=>
(1, 2, 3, 4, 5)
{}

show(a=3,b=2, c=8, d=78, e=0)
=>
()
{'a': 3, 'c': 8, 'b': 2, 'e': 0, 'd': 78}


示意:
caller: show(1,2,3,4,5)

callee: show(*args)
這裡我們可以看到 *arg = 1,2,3,4,5
拔掉外框的arg = 1,2,3,4,5
所以原來的arg = (1,2,3,4,5)


在這裡*args收到的elements, 只會加tuple外框, 而**kwargs收到的引數, 是加字典的外框

"""


"""
args = args + ('yo', 'cc')
既然只是tuple而已, 那麼當然也可以對args對增加刪減,然後再傳出的動作


def show(a, b, *args, **kwargs):
    print a
    print b
    print args

show(1,2,3,4)
=>
1
2
(3, 4)
"""














