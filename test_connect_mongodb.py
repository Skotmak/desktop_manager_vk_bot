from enum import unique
import pymongo
import datetime
from itertools import count

from pymongo.message import _query_compressed, query


client = pymongo.MongoClient("mongodb+srv://user:2467531max@cluster0.najw2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") 
db = client.testdata
coll = db.users


#print(coll.index_information())
#coll.drop_index("login_1")
#print("ok")
#print(coll.index_information())
#coll.insert_one({"login": "name0"})
#coll.create_index([('login', pymongo.DESCENDING)])
print(coll.find_one({"login": "name330"}))
#закончил 9й урок




'''
#coll.create_index([("login", pymongo.ASCENDING)], unique=True) #создание уникальных индексов
#print(coll.index_information())
###

#coll.drop_index("login_-1") #удаление индекса
#coll.create_index([('login', pymongo.DESCENDING)]) #добавление индекса
print(coll.index_information())
###

for i in count(0, 1):
    data = {
        "_id": i,
        "login": f"name{i}",
        "password": f"passw{i}",
        "time": datetime.datetime.now()
    }
    coll.insert_one(data)
    print(f"{i} : data has beed recorded")
###

res = coll.delete_many({})
print("deleted: ", res.deleted_count)
###

query = {"name": {"$regex": "new"}}
res = coll.delete_many(query)
print("deleted: ", res.deleted_count)
###

coll.delete_one({"_id": 0 })
###

current = {"_id": 1}
new_data = {"$push": {"arrage": 'hello'}}

coll.update_many(current, new_data)
###

current = {"_id": 1}
new_data = {"$inc": {"balance": 2200}} # или вместо 2200 можно отрицательное значение добавить и тогда произойдёт вычитание

coll.update_many(current, new_data)
###
current = {"name": {"$regex": "test."}}
new_data = {"$set": {"name": "new"}}

coll.update_many(current, new_data)
###

current = {"name": "test3"}
new_data = {"$set": {"name": "new"}}

coll.update_one(current, new_data)
###

for i in range(20):
    coll.insert_one({"_id": i, "name": f'test{i}' })
###

coll.drop()
print("коллекция удалена")
###

res = db.list_collection_names()
print(res)
###

res = client.list_database_names()
print(res)
###

res = coll.count_documents({"name": {"$regex": "t"}})
print(res)
###

for value in coll.find().sort("_id", -1):
    print(value)
###

res = coll.find_one({"name": "test3"})
print(res)
###




query = {'status': True}
query1 = {'name': 'Max'}
query2 = {"name": {"$gt": "A"}}
query3 = {"name": {"$regex": "test."}}
for value in coll.find(query3):  #(query, {"_id": 0, "status": 1})
    print(value)


###coll.insert_one({"_id": 2, "name": "Max"})

data = {
        '_id': 5,
        'status': True,
        'time': datetime.datetime.now(),
        'flags': [1, 2, 3]
    }
coll.insert_one(data)
###


coll.insert_many(data)
res = coll.find()

for value in res:
    print(value)


coll.insert_one({"_id": 1, "name": "Alex"})
#coll = db.new_users
#coll.insert_one({"_id": 1, "name": "Alex"})
'''