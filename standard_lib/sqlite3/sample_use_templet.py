# coding:utf-8
import sqlite3


class QueryTemplateBase(object):
    """
        模板类。process_format定义模板执行顺序
    """

    def connect(self):
        pass

    def construct_query(self):
        pass

    def do_query(self):
        pass

    def format_results(self):
        pass

    def output_results(self):
        pass

    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_results()


class QueryTemplate(QueryTemplateBase):

    def connect(self):
        self.conn = sqlite3.connect("sales.db")

    def construct_query(self):
        # 提示需要被子类重写。排错比较有用
        raise NotImplementedError()

    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(", ".join(row))
        self.formatted_results = "\n".join(output)

    def output_results(self):
        raise NotImplementedError()


class NewVehiclesQuery(QueryTemplate):

    def construct_query(self):
        self.query = "select * from Sales WHERE new = 'true'"

    def output_results(self):
        print(self.format_results)


if __name__ == '__main__':
    pass

