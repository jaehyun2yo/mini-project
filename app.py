from flask import Flask, render_template
# const Flask = require('Flask');
# from pymongo import MongoClient

app = Flask(__name__)

client=MongoClient("mongodb://localhost", 27017) #client로 MongoDB 접속
db=client.jaehyun #client의 저장소 생성

doc = {
    'name' : 'jaehyun',
    'age' : 29
}

db.users.insert_one(doc);

@app.route('/')
def home():
   return render_template('index.html')


if __name__ == '__main__':  
  app.run('0.0.0.0',port=5001,debug=True)