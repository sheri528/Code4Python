# coding:utf-8

"""
        1.单例模式的静态语言实现：
            构造函数私有化，提供静态方法获取单例。这个方法在第一次调用时创建实例，后续再被调用则返回同一个实例
        2.Python无私有构造函数，可通过__new__方法实现
        3.注意：
            单例模式可能干扰分布式计算、并行编程、自动化测试
"""

class OneOnly(object):

    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
        return cls._singleton


if __name__ == '__main__':
    o1 = OneOnly()
    o2 = OneOnly()

    # o1,o2具有相同内存地址
    print(o1 == o2)
    print(id(o1) == id(o2))