from pymongo import MongoClient

client = MongoClient("mongodb+srv://jaehyun:1234@cluster0.lgsc4xh.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.mydb



# 데이터 넣기 
# db.users.insert_one(users)