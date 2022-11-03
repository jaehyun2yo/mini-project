from flask import Flask, render_template, jsonify, request
from  pymongo  import MongoClient
import certifi


app = Flask(__name__, static_folder='static', static_url_path="/static")

client = MongoClient("mongodb+srv://jaehyun:1234@cluster0.lgsc4xh.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.mydb
# 임시 데이터
users ={
    "id": 1,
   "username" : "김재현",
   "mbti" : "INTP",
   "dec1" : "호기심이많고 보여지는부분에 관심이있어 프론트엔드를 준비하게되었습니다. ",
   "dec2" : "흥미있는 분야는 깊게 파고드려하는 성격이 장점이라 할수있고 ",
   "dec3" : "협업시 좋은 결과물을 만들기위해서 개인적으로 욕심을 내는 스타일 입니다.",
   "blogUrl" : "https://jaehyun2yo.tistory.com/" ,
   "github" : "https://github.com/jaehyun2yo",
   
   }  

# 홈 
@app.route('/')
def home():
   return render_template('index.html')


# 유저 읽기 
@app.route('/user/<int:id>')
def user_page(id):
      return render_template('jaehyun.html',users=users)

@app.route('/user/1', methods=["POST"])
def comment_save():
       comment_receive = request.form['comment_give']
       comment_data = {
          "comment":comment_receive
       }
       db.comment.insert_one(comment_data)
       return jsonify({ 'msg' : "작성완료 "})


@app.route('/user/1/comments', methods=["GET"])
def comment_get():
       comment_list = list(db.comment.find({}, {"_id" : False}))
       return jsonify({'comments' : comment_list})
    
    
if __name__ == '__main__':  
   app.run('0.0.0.0',port=8000,debug=True)
  
