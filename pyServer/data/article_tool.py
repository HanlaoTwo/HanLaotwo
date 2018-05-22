from datatool import datatool
import json
from article import article

class articleTool(datatool):

    query_by_title_sql = "SELECT * FROM article WHERE title = ?"
    query_all_title_sql = "select title from article"
    query_all_sql = "select * from article"


    def query(self, title):
        self.cursor.execute(self.query_by_title_sql, (title,))
        data = self.cursor.fetchall()[0]
        art = article(data[1],data[2],data[3],data[4])
        return art.__dict__

    def query_all_title(self):
        self.cursor.execute(self.query_all_title_sql)
        data = self.cursor.fetchall()
        lists = []
        for node in data:
            lists.append({"title":node[0]})
        return lists

    def query_all(self):
        self.cursor.execute(self.query_all_sql)
        data = self.cursor.fetchall()
        data = str(data)
        data = super().listToJson(data)
        return data

tool = articleTool()
print(tool.query(title='test'))
