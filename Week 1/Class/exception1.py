import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient(host="localhost",port =27017)
db = connection.test
users = db.users

doc = {'nombre': "Luis Arturo", 'apellido': "Perez Diaz"}
print doc
print "\n Insertando documento"

try:
    users.insert_one(doc)
except Exception as ex:
    print "\n ERROR: Algo salio mal: ", ex

print "\n"
print doc
print "\n Insertandolo otra vez"
doc = {'nombre': "Luis Arturo", 'apellido': "Perez Diaz"}


try:
    users.insert_one(doc)
except Exception as ex:
    print "\n ERROR: Algo salio mal: ", e