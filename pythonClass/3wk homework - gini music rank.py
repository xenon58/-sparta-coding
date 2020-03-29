import requests
from bs4 import BeautifulSoup

# 지니 뮤직 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, 원하는 정보 (곡 제목, 가수) 불러오기
music_list = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

#  음악들 반복문을 돌리기
rank = 0
for music in music_list :
    title1 = music.select('td.info > a.title.ellipsis')
    singer1 = music.select ('td.info > a.artist.ellipsis')

    title2 = title1[0].text.strip()
    singer2 = singer1[0].text.strip()
    rank += 1
    print (rank, title2, '-', singer2)