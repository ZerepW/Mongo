import pymongo
import sys
from pymongo import MongoClient

connection = MongoClient("mongodb://localhost")
db = connection.students
grades = db.grades


def find():
    print "Buscando ... \n"
    query = {'type':"homework"}
    try:
        cursor = grades.find(query).sort([['student_id',pymongo.ASCENDING], ['score',pymongo.ASCENDING]])
    except Exception as e:
        print "ERROR: Ops, hubo un error: ", type(e), e  
    
    i = 0
    for doc in cursor: 
        if(i == 0):
            grades.remove(doc)
        i = i+1
        if(i == 1):
            print doc
        if(i == 2):
            i = 0

find()

    #.sort({student_id:1, score:1})
