from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.project

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/pt_data', methods=['GET'])
def saved_data():
    # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    result=list(db.intervention.find({},{'_id':False}))
    return jsonify({'result': 'success','raw_data':result})


@app.route('/pt_data', methods=['POST'])
def patient_data():
    # 1. 클라이언트가 전달한 _give 정보를 _receive 변수에 넣습니다.
    date_receive = request.form['date_give']
    number_receive = request.form['number_give']
    room_receive = request.form['room_give']
    name_receive = request.form['name_give']
    sex_receive = request.form['sex_give']
    age_receive = request.form['age_give']
    site_receive = request.form['site_give']
    interv_name_receive = request.form['interv_name_give']
    info_receive = request.form['info_give']

    # 2. 전달 받은 정보를 db에 저장한다.
    pt_data = {'date': date_receive,
               'number': number_receive,
               'room':room_receive,
               'name':name_receive,
               'sex':sex_receive,
               'age':age_receive,
               'site':site_receive,
               'interv_name': interv_name_receive,
               'info':info_receive}

    db.intervention.insert_one(pt_data)
    return jsonify({'result':'success', 'msg':'스케줄에 등록 되었습니다!'})


# @app.route('/api/delete', methods=['POST'])
# def star_delete():
#     # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
#     name_receive = request.form['name_give']
#     # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
#     db.mystar.delete_one({'name':name_receive})
#     # 3. 성공하면 success 메시지를 반환합니다.
#     return jsonify({'result': 'success','msg':'삭제 완료! 안녕~'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)