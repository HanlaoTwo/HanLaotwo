import sqlite3


class datatool:
    query_all_sql = "select * from art"

    def __init__(self):
        self.conn = sqlite3.connect('myweb.db')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()
