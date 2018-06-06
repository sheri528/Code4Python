# coding:utf-8
import create_db

"""
    1.基于文件的数据库引擎。也称嵌入式数据库

"""

conn = create_db.connect("sales.db")

conn.execute("CREATE TABLE Sales (salesperson text, amt currency, year integer, model text, new boolean)")

conn.execute("Insert into Sales VALUES "
             "('Tim', 1600, 2010, 'Honda Fit', 'true')")

conn.commit()

conn.close()