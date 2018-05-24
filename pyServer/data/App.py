import json
from flask import Flask, request, url_for
from article_tool import articleTool
import ListContent
import constant

app = Flask(__name__)

article_tool = articleTool()


def make_header(data):
    res = app.make_response(data)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user', methods=['POST'])
def hello_user():
    return 'hello user'


@app.route('/users/<id>')
def user_id(id):
    return 'hello user:' + id


@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return 'query user:' + id


@app.route('/query_url')
def query_url():
    return 'query url:' + url_for('query_user')


@app.route('/get_content')
def get_content():
    data = ""
    res = app.make_response(data)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


@app.route('/get_list')
def get_list():
    lsit = article_tool.query_all_title()
    data = json.dumps(lsit)
    return make_header(data=data)


# # *************************by sql**********************
# @app.route('/get_article/<title>')
# def article(title):
#     article = article_tool.query(title=title)
#     data = json.dumps(article)
#     return make_header(data=str(data))

@app.route('/get_conetnt')
def get_conetnt():
    content = ListContent.get_content()
    data = json.dumps(content)
    return make_header(data=str(data))


# *********************************** by read file *************************
# usrl patern: get_article?dir=blog&name=haha
@app.route('/get_article')
def article():
    dir = request.args.get('dir')
    name = request.args.get('name')
    path = constant.COTENT_DIR + '\\' + dir + '\\' + name
    f = open(path, encoding='UTF-8')
    article = f.read()
    return make_header(data=str(article))


if __name__ == '__main__':
    app.run()
