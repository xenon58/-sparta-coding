from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('original.html')

## API 역할을 하는 부분
@app.route('/content', methods=['POST'])
def message_post():
   name_receive = request.form['name_give']
   select_receive = request.form['select_give']
   address_receive = request.form['address_give']
   number_receive = request.form['number_give']
   doc={'name': name_receive, 'select': select_receive,'address': address_receive,'number': number_receive}
   db.homework.insert_one(doc)
   return jsonify({'result':'success','msg': '리뷰가 성공적으로 작성되었습니다.'})

@app.route('/content', methods=['GET'])
def message_get():
   send_data = list(db.homework.find({},{'_id':False}))
   return jsonify({'result':'success', 'msg': send_data})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)