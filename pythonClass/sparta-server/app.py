from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/write')
def write():
   return '질문은 이쪽으로 보내주세요~ xenon58@naver.com'

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000, debug=True)
