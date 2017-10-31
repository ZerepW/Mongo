import pymongo
import sys
from pymongo import MongoClient

connection = MongoClient("mongodb://localhost")
db = connection.reddit
stories = db.stories

def find():
    print "Buscando ... \n"
    query = {'title': {'$regex': 'tech|robot', '$options': 'i'}}
    projection = {'title': 1, '_id': 0}

    try:
        cursor = stories.find(query, projection)
    except Exception as e:
        print "ERROR: Ops, hubo un error: ", type(e), e 

    for doc in cursor: 
        print doc
find()

db.grades.aggregate([{'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1}])
