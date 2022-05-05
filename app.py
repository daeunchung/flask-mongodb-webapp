from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML 을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분


@app.route('/review', methods=['POST'])
def write_review():
    # sample_receive = request.form['sample_give']
    # print(sample_receive)
    # return jsonify({'msg': '이 요청은 POST!'})
    # 1. 클라이언트가 준 title, author, review 가져오기
    # 2. DB에 정보 삽입하기
    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})



@app.route('/review', methods=['GET'])
def read_reviews():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)