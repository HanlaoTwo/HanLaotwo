import os
import constant

homedir = constant.COTENT_DIR


class FileNode():
    child = []
    name = ""

    def __init__(self, name, files):
        self.name = name
        self.files = files


def get_content():
    content = []
    tree = os.walk(homedir, topdown=False)
    for i in tree:
        nodeName = i[0]
        nodeDirs = i[1]
        nodeFiles = i[2]
        name = nodeName.split('\\')
        node = FileNode(name[len(name)-1], nodeFiles)
        content.append(node.__dict__)
    return content


def getBySql():
    import sqlite3
    conn = sqlite3.connect('myweb.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM testcontent ORDER BY depth')
    data = cursor.fetchall()
    print(data)

print(get_content())