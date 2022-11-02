from flask import Flask, render_template, jsonify
# const Flask = require('Flask');
# from pymongo import MongoClient

app = Flask(__name__, static_folder='static', static_url_path="/static")

# client=MongoClient("mongodb://localhost", 27017) #client로 MongoDB 접속
# db=client.jaehyun #client의 저장소 생성

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/<username>")
def show_user_page(username):
    return jsonify({"status": "healthy"})

if __name__ == '__main__':  
  app.run('0.0.0.0',port=5001,debug=True)