#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

"""
    from : https://github.com/faif/python-patterns/blob/master/structural/decorator.py
    作用：
        1.将一个核心对象和其他可以改变这个对象的功能对象（装饰对象）“包裹”在一起，增强核心对象的功能
        2.支持多种可选行为。这个也可以用多重继承替代（Mixin）

    静态语言实现：
        核心对象及装饰对象实现相同接口。当被调用时，装饰器在调用它的封装接口之前或之后做一些额外处理。

    注意：
        1.装饰器可以在不修改实现的前提下动态给对象增加特性
        2.与继承的区别是，装饰器可以只修改某个对象，而不像继承是修改整个子类

"""


"""
*What is this pattern about?
The Decorator pattern is used to dynamically add a new feature to an
object without changing its implementation. It differs from
inheritance because the new feature is added only to that particular
object, not to the entire subclass.

*What does this example do?
This example shows a way to add formatting options (boldface and
italic) to a text by appending the corresponding tags (<b> and
<i>). Also, we can see that decorators can be applied one after the other,
since the original text is passed to the bold wrapper, which in turn
is passed to the italic wrapper.

*Where is the pattern used practically?
The Grok framework uses decorators to add functionalities to methods,
like permissions or subscription to an event:
http://grok.zope.org/doc/current/reference/decorators.html

*References:
https://sourcemaking.com/design_patterns/decorator

*TL;DR80
Adds behaviour to object without affecting its class.
"""


class TextTag(object):
    """Represents a base text tag"""
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())

if __name__ == '__main__':
    simple_hello = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("before:", simple_hello.render())
    print("after:", special_hello.render())

### OUTPUT ###
# before: hello, world!
# after: <i><b>hello, world!</b></i>

