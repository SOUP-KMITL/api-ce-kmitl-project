
# -*- coding: utf-8 -*-
#from pyspark import SparkContext
#from pyspark.sql import *
#from pyspark.sql.types import *
import dateutil.parser as date
import json
from pymongo import MongoClient 
from pprint import pprint

#spark = SparkSession\
#    .builder\
#    .master("spark://stack-02:7077")\
#    .config("spark.cores.max", 2)\
#    .appName("SocialDataService")\
#    .getOrCreate()

#sc = spark.sparkContext


#def getSocialDataByStartAndEnd(start, end):
#    socialDataParquet = "hdfs://stack-02:9000/SocialDataRepository/SOCIALDATA.parquet"
#    socialDataDF = spark.read.parquet(socialDataParquet)
#    socialDataDF = socialDataDF.sort(socialDataDF.created_at.desc())
#    socialData = socialDataDF.where(start >= socialDataDF.created_at).where(socialDataDF.created_at <= end).collect()
#    sd_list = []
#    for sd in socialData:
#        sd_list.append(sd.asDict())
#    return sd_list

def getTweetDataByStartAndEnd(start, end):
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['SocialData']
    tweet_collection = db.tweet
    tweets = tweet_collection.find({"created_at": {"$gte": date.parse(start), "$lte": date.parse(end)}})
    tw_list = []
    for tw in tweets:
        del tw['_id']
        tw_list.append(tw)
    return tw_list

#def getAllSocialData():
#    socialDataParquet = "hdfs://stack-02:9000/SocialDataRepository/SOCIALDATA.parquet"
#    socialDataDF = spark.read.parquet(socialDataParquet)
#    socialData = socialDataDF.collect()
#    sd_list = []
#    for sd in socialData:
#        sd_list.append(sd.asDict())
#    return sd_list

def getThingStations():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['Environment']
    collection = db.ThingStation
    data = collection.find({},{'_id':0})
    data_list = []
    for item in data:
    	data_list.append(item)
    return data_list

def getTelemetryByThingId():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['Environment']
    collection = db.ThingTelemetry
    data = collection.find({},{'_id':0}).sort("_id", -1).limit(1)
    data_list = []
    for item in data:
    	data_list.append(item)
    return data_list

def getTaxiData():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['SmartMobility']
    collection = db.taxiData
    data = collection.find({},{'_id':0}).sort("_id", -1).limit(1)
    data_list = []
    for item in data:
    	data_list.append(item)
    return data_list

def getTaxiDensity():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['SmartMobility']
    collection = db.taxiDensity
    data = collection.find({},{'_id':0}).sort("_id", -1).limit(1)
    data_list = []
    for item in data:
    	data_list.append(item)
    return data_list

def getAllQuery():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['SocialData']
    query_collection = db.query
    query = query_collection.find()
    query_list = []
    for q in query:
        del q['_id']
        query_list.append(q)
    return query_list

def getPlaceById(place_id):
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['SocialData']
    place_collection = db.place2
    place = place_collection.find({"place_id":place_id})
    place_list = []
    for p in place:
        del p['_id']
    	place_list.append(p)
    return place_list

def getAllLocations():
    client = MongoClient('mongodb://127.0.0.1:27017/')     
    db = client['SocialData']     
    place_collection = db.place2
    place = place_collection.find()
    place_list = []
    for p in place:
        del p['_id']
        coord = (p['geolocation']).split(",")
        p['lat'] = coord[0]
        p['lng'] = coord[1]
        place_list.append(p)
    return place_list

def get_predicted():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['SocialData']
    predicted_collection = db.predicted
    predicted = predicted_collection.find({'predicted':{'$gt':[]}}).sort("_id", -1).limit(1)
    for p in predicted:
        predicted = p
    del predicted['_id']
    return predicted

def save_predicted(predicted):
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['SocialData']
    predicted_collection = db.predicted
    result = predicted_collection.insert_one({'id': predicted['id'], 'predicted': predicted['predicted']}).inserted_id
    return result
