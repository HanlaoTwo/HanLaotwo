from datatool import datatool

class articleTool(datatool):

    query_by_title_sql = "SELECT * FROM article WHERE title = ?"
    query_all_title_sql = "select title from article"
    query_all_sql = "select * from article"


    def query(self, title):
        self.cursor.execute(self.query_by_title_sql, (title,))
        return self.cursor.fetchall()

    def query_all_title(self):
        self.cursor.execute(self.query_all_title_sql)
        return self.cursor.fetchall()

    def query_all(self):
        self.cursor.execute(self.query_all_sql)
        return self.cursor.fetchall()


tool = articleTool()
print(tool.query_all())
print(tool.query_all_title())
print(tool.query(title='test'))
