from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML 을 주는 부분


@app.route('/')
def home_review():
    return render_template('index_review.html')

@app.route('/api')
def home_mystar():
    return render_template('index_mystar.html')

# 리뷰 API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    # 1) 클라이언트와 서버 확인
    # sample_receive = request.form['sample_give']
    # print(sample_receive)
    # return jsonify({'msg': '이 요청은 POST!'})

    # 2) 서버부터 만들기
    # 1. 클라이언트가 준 title, author, review 가져오기
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    # 2. DB에 정보 삽입하기
    doc = {
        'title' : title_receive,
        'author' : author_receive,
        'review' : review_receive
    }
    db.bookreview.insert_one(doc)

    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/review', methods=['GET'])
def read_reviews():
    # 1) 클라이언트와 서버 확인
    # sample_receive = request.args.get('sample_give')
    # print(sample_receive)
    # return jsonify({'msg': '이 요청은 GET!'})

    # 2) 서버부터 만들기
    # 1. DB에서 리뷰 정보 모두 가져오기
    reviews = list(db.bookreview.find({}, {'_id': False }))
    # 2. 성공 여부 & 리뷰 목록 반환
    return jsonify({'all_reviews': reviews})


# mystar API 역할을 하는 부분
# 뼈대 세우기

@app.route('/api/list', methods=['GET'])
def show_stars():
    movie_star = list(db.mystar.find({}, {'_id': False}).sort('like',-1))
    return jsonify({'movie_stars': movie_star})


@app.route('/api/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give']

    target_star = db.mystar.find_one({'name': name_receive})

    current_like = target_star['like']
    new_like = current_like + 1

    db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_give']
    db.mystar.delete_one({'name': name_receive})

    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)