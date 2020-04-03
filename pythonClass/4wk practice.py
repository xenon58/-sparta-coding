from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

musics = list(db.music_chart.find())

target_music = db.music_chart.find_one({"title":"Black Swan"})
target_singer = target_music['singer']

titles = list(db.music_chart.find({'singer':target_singer}))

for title in titles :
    print(title[target_singer))