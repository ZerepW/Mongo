import pymongo

from pymongo import MongoClient

#Connect DB
connection = MongoClient('localhost',27017)
db = connection.test

#Names Collection
names = db.names

item = names.find_one()
print item['name']