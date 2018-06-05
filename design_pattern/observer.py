# coding:utf-8
import weakref
import os
import sys

'''
    应用：冗余备份系统

    使用方式：编写一个核心对象维护一些特定的属性值，当调用property.setter时，通知观察者。

    作用：分离被观察的代码和执行观察的代码

    debug Error:
    1. setter
        descriptor 'setter' requires a 'property' object
    2. i/c循环引用
'''

class Inventory(object):

    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            # observer为可调用对象，需要实现__call__
            observer()


class ConsoleObserver(object):

    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self, *args, **kwargs):
        print(self.inventory.product)
        print(self.inventory.quantity)


if __name__ == '__main__':
    i = Inventory()
    print("创建时i的引用计数：{}".format(sys.getrefcount(i)))

    c = ConsoleObserver(i)
    print("创建时c的引用计数：{}".format(sys.getrefcount(c)))
    print("i的引用计数：{}".format(sys.getrefcount(i)))

    i.attach(c)
    print("attach")
    print("c的引用计数：{}".format(sys.getrefcount(c)))
    print("i的引用计数：{}".format(sys.getrefcount(i)))

    i.product = "Widget"
    i.quantity = 5


