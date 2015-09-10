# -*- coding: utf8 -*-


u"""但是同时使用元素的序号和元素本身也是常见的需求。
我们经常看到一些程序员使用len()和range()来通过下标迭代列表，
但是有一种更简单的方式。"""

drinks = ["coffee", "tea", "milk", "water"]
for index, drink in enumerate(drinks):
    print index, drink
#Item 0 is coffee
#Item 1 is tea
#Item 2 is milk
#Item 3 is water