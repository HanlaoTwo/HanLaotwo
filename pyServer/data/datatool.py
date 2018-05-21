import sqlite3


class datatool:
    query_all_sql = "select * from art"

    def __init__(self):
        self.conn = sqlite3.connect('D:\workspace\HSElite\Sources\PDD_Biz\pdd-hmd\pdd-hmd-ofl\input\script\\test.db')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()
