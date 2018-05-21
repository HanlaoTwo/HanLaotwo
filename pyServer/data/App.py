import json
from flask import Flask,request,url_for
from article_tool import articleTool


app = Flask(__name__)
article_tool = articleTool()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user', methods=['POST'])
def hello_user():
    return 'hello user'

@app.route('/users/<id>')
def user_id(id):
    return 'hello user:'+id

@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return 'query user:'+id

@app.route('/query_url')
def query_url():
    return 'query url:'+url_for('query_user')\

@app.route('/get_content')
def get_content():
    data =  ""
    res = app.make_response(data)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


@app.route('/get_list')
def get_list():
    lsit = article_tool.query_all()
    data = json.dumps(lsit)
    res = app.make_response(data)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

if __name__ == '__main__':
    app.run()
