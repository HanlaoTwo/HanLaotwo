import os

homedir = 'D:\workspace\idea\Hanlaotwo\Pages\htmls'

def get_size(filedir):
    tree = os.walk(filedir, topdown=False)
    loopNum = 1
    for i in tree:
        nodeName = i[0]
        nodeDirs = i[1]
        nodeFiles = i[2]
        print('dir: ',nodeName)
        for file in nodeFiles:
            print('file ',file)
        print('*****************************',loopNum)
        loopNum = loopNum + 1


get_size(homedir)

