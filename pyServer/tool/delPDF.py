import os

tree = os.walk('C:\\Users\\hanqian18790\\Desktop\\note', topdown=False)
for i in tree:
    nodeName = i[0]
    nodeDirs = i[1]
    nodeFiles = i[2]
    for file in nodeFiles:
        # print(file)
        if file.endswith('.pdf'):
            print(file)
            os.remove(nodeName+"\\"+file)