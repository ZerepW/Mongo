import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient(host ="localhost", port=27017)
db = connection.school
scores = db.scores

def find():
    print "Encontrar tipo examen"
    query = {'type': 'exam', 'score': {'$gt':70, '$lt':90}}
    projection = {'student_id':1,'_id':0}
    try:
        cursor = scores.find(query, projection)
    except Exception as ex:
        print "ERROR: Hubo un error: ", type(ex), ex
    sanity = 0
    for doc in cursor:
        #print "Alumno ID: " + doc.student_id + " Tipo: " + doc.type + " Calificacion: " + doc.score + "\n"
        print doc
        sanity += 1
        if (sanity > 10):
            break

def find_one():
    print "Encontrar un estudiante"
    query = {'student_id': 10}
    projection = {'student_id':1,'_id':0}
    try:
        doc = scores.find_one(query, projection)
    except Exception as ex:
        print "ERROR: Hubo un error: ", type(ex), ex
    print doc

find()