import certifi
import requests as requests
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.r0t0c.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/board.html')
def board():
    return render_template('board.html')

@app.route('/write.html')
def write():
    return render_template('write.html')

@app.route('/view.html')
def view():
    return render_template('view.html')

@app.route("/myungjin", methods=["POST"])
def myungjin_post():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    # 글번호 먹이는 코드
    myungjin_list = list(db.myungjin.find({}, {'_id':False}))
    post_cnt = len(myungjin_list)

    doc = {
        'post_num': post_cnt+1,
        'title': title_receive,
        'content': content_receive,
    }
    db.myungjin.insert_one(doc)
    return jsonify({'msg': '정상적으로 등록되었습니다.'})

@app.route("/myungjin", methods=["GET"])
def myungjin_get():
    content_list = list(db.myungjin.find({}, {'_id': False}))
    return jsonify({'myungjin': content_list})

@app.route("/myungjin/num", methods=["GET"])
def myungin_num():


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)