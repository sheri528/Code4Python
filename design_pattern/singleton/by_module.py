# coding:utf-8

"""
    1.为什么在类的内部，变量被定义前访问模块变量（child_node）？
        类内部代码在方法调用前不会被执行

    2.本方法需要在模块中创建实例（child_node）,模块外不能限制实例的创建为单例。

"""

class Node(object):
    pass

class FirstTag(object):
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find('<')
        i_end_tag = remaining_string.find('>')
        tag_name = remaining_string[i_start_tag+1:i_end_tag]
        # root = Node(tag_name)
        # parser.root = parser.current_node = root
        parser.state = child_node
        print(id(parser.state))


class ChildNode(object):
    def process(self, remaining_string, parser):
        stripped = remaining_string.strip()
        if stripped.startswith("</"):
            parser.state = close_tag
        elif stripped.startswith("<"):
            parser.state = open_tag
        else:
            parser.state = text_node
        return stripped

class OpenTag(object):
    def process(self, remaining_string, parser):
        parser.state = child_node


class TextNode(object):
    def process(self, remaining_string, parser):
        parser.state = child_node


class CloseTag(object):
    def process(self, remaining_string, parser):
        parser.state = child_node

first_tag = FirstTag()
child_node = ChildNode()
print(id(child_node))
text_node = TextNode()
open_tag = OpenTag()
close_tag = CloseTag()

if __name__ == '__main__':
    f1 = FirstTag()
    f2 = FirstTag()
    f3 = FirstTag()
    node = Node()

    # 本例中parse.state状态对象是单例
    res1 = f1.process('<abc>', node)
    res2 = f2.process('<abcd>', node)
    res3 = f3.process('<abcde>', node)