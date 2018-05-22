import sqlite3
import json

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

# [('test',), ('test',), ('test',), ('test',)]
    def listToJson(self,listData):
        return listData.replace("(","{").replace(")","}")
        # for data in listData:
        #     article = article(data[0],data[1],data[2],data[3])
        #     pass
