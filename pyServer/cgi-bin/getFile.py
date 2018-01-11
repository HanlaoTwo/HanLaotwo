
clog = '### hello'
f = open('D:/workspace/idea/HanLaotwo/Pages/content/haha',encoding='UTF-8')
clog = f.read()

#print('Accept: application/json, text/javascript, */*; q=0.01')
print('Content-Type: text/html;charset=GBK')
#print('Access-Control-Allow-Credentials: true')
#print('Access-Control-Allow-Headers: accessToken,Content-Type')
print('Access-Control-Allow-Origin: *' + '\n')
print(clog)
print("监听程序无法找到匹配协议栈的可用句柄.")
