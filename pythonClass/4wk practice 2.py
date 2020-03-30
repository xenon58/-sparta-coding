from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##
movie_point=db.movies.find_one({'title':'어벤져스: 엔드게임'})
movie_star= movie_point['star']

print(movie_star)

movies = db.movies.find({'star':movie_star})

db.movies.update_many()