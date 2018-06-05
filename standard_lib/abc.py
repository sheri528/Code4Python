# -*- coding: utf-8 -*-
import abc

'''

    抽象基类：
        1.作用：为一组子类建立一个公共API, 并完成接口验证。
        2.不能实例化，可提供默认实现
        3.工作过程：
            a.定义一组API并标志为抽象，然后注册具体类为抽象类的实现
            b.派生实现

'''


class PluginBase(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def load(self, input):
        """retrieve data from the input source
        and return an object."""
        pass

    @abc.abstractclassmethod
    def save(self, output, data):
        """save data to output"""
        pass


class LocalBaseClass(object):
    pass


class RegisteredImplementation(LocalBaseClass):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

# ?
PluginBase.register(RegisteredImplementation)

if __name__ == '__main__':
    print('Subclass: {}'.format(issubclass(RegisteredImplementation, PluginBase)))
    print('Instance: {}'.format(isinstance(RegisteredImplementation, PluginBase)))