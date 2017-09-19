#!/usr/bin/env python
import datetime
import pandas as pd
from pymongo import MongoClient
from pymongo import ASCENDING 
from pymongo import DESCENDING 


class Mongo:
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass 

    def readallrecords(self):
        client = MongoClient('localhost', 27017)
        db = client.mydb
        cursor = db.mytodo.find()
        df = pd.DataFrame(list(cursor))
        client.close()
        return df
    
    def reccount(self):
        client = MongoClient('localhost', 27017)
        db = client.mydb
        cursor = db.mytodo.find()
        df = pd.DataFrame(list(cursor))
        client.close()
        cn = len(df)
        return cn       

    def readallrecordsbk(self):
        client = MongoClient('localhost', 27017)
        db = client.mydb
        cursor = db.mytodobackup.find()
        df = pd.DataFrame(list(cursor))
        client.close()
        return df    

    def findarecord(self, rec1):
        client = MongoClient('localhost', 27017)
        db = client.mydb
        cursor = db.mytodo.find(rec1)
        self.df = pd.DataFrame(list(cursor))
        client.close()
        return self.df

    def findarecordbk(self, rec1):
        client = MongoClient('localhost', 27017)
        db = client.mydb
        cursor = db.mytodobackup.find(rec1)
        self.df = pd.DataFrame(list(cursor))
        client.close()
        return self.df    

    def newrecord(self, rec1):
        client = MongoClient('localhost', 27017)
        db = client.mydb
        cursor = db.mytodo.insert(rec1)
        #self.mydf = pd.DataFrame(list(cursor))
        client.close()
        return

    def newrecordbk(self, recbk):
        client = MongoClient('localhost', 27017)
        db = client.mydb
        cursor = db.mytodobackup.insert(recbk)
        client.close()
        return    
    
    def deleteone(self, rec1):
        client = MongoClient('localhost', 27017)
        db = client.mydb
        cursor = db.mytodo.delete_one(rec1)
        client.close()
        return

    def updateone(self, rec):
        client = MongoClient('localhost', 27017)
        db = client.mydb
        myid = rec['_id']
        tdnam = rec['todoname']
        tddisc = rec['tododisc']
        sdate = rec['startdate']
        edate = rec['enddate']
        act = rec['active']
        chdate = rec['changeddate']
        cursor = db.mytodo.update({'_id': myid},{'$set': { 'todoname': tdnam, 'tododisc': tddisc, 'active': act, 'startdate': sdate, 'enddate': edate, 'changeddate': chdate }})
        client.close()
        return

    def updateonebk(self, rec):
        client = MongoClient('localhost', 27017)
        db = client.mydb
        cursor = db.mytodobackup.insert(rec)
        client.close()
        return    
    
    def findlastrecid(self):
        client = MongoClient('localhost', 27017)
        db = client.mydb
        re = db.mytodobackup.create_index('recid')
        x = db.mytodobackup.find().sort('recid', 1)
        mydcid = pd.DataFrame(list(x))
        for rec in range(0, len(mydcid)):
            self.recidn = mydcid.get_value(rec,'recid')
            print(self.recidn)
        client.close()
        return   self.recidn       

if __name__ == '__main__':
    tdate = datetime.date.today()
    tdaytime = datetime.datetime.now()
