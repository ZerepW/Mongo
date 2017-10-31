import bottle
import pymongo
from pymongo import MongoClient

@bottle.route('/')
def index():
    #Connect DB
    connection = MongoClient('localhost',27017)
    #Choose Collection
    db = connection.test
    #Choose Document
    name = db.names

    #SELECT ONE
    item = name.find()

    return '<b>Hello %s!</b>' % item[0]['name']

bottle.run(host='localhost', port=8082)