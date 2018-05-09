import sqlite3
class datatools:

    insert_sql = "INSERT INTO art (name, path, date) VALUES (?,?,?)"
    del_sql = "DELETE FROM art WHERE name = ?"
    query_sql = "SELECT * FROM art WHERE name = ?"
    mod_sql = ""

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

    def add(self,name,path,date):
        self.cursor.execute(self.insert_sql,(name,path,date))
        self.commit()

    def dele(self,name):
        self.cursor.execute(self.del_sql,(name))
        self.commit()

    def query(self,name):
        self.cursor.execute(self.query_sql,(name))

    def query_all(self):
        self.cursor.execute(self.query_all_sql)
        return self.cursor.fetchall()

    def mod(self):
        self.commit()
        pass

tool = datatools()
tool.add('1','23423','asdasd')
print(tool.query_all())

