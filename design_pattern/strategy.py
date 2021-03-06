#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' from https://github.com/faif/python-patterns/blob/master/behavioral/strategy.py

    策略模式：
        每一个类（函数）封装一种算法，每个算法为一种策略。是常见的插件实现模式。
        目的： 将定义和使用分开。即分离行为与环境。

'''

"""
http://stackoverflow.com/questions/963965/how-is-this-strategy-pattern
 -written-in-python-the-sample-in-wikipedia
In most of other languages Strategy pattern is implemented via creating some
base strategy interface/abstract class and subclassing it with a number of
concrete strategies (as we can see at
http://en.wikipedia.org/wiki/Strategy_pattern), however Python supports
higher-order functions and allows us to have only one class and inject
functions into it's instances, as shown in this example.
*TL;DR80
Enables selecting an algorithm at runtime.

"""

import types


class StrategyExample:

    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            # 传递的函数指针绑定到了类的同名方法属性，因此调用execute()时执行的是传入的函数
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')


if __name__ == '__main__':
    strat0 = StrategyExample()

    strat1 = StrategyExample(execute_replacement1)
    strat1.name = 'Strategy Example 1'

    strat2 = StrategyExample(execute_replacement2)
    strat2.name = 'Strategy Example 2'

    strat0.execute()
    strat1.execute()
    strat2.execute()