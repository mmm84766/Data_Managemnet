import requests
from datetime import datetime
from datetime import timedelta
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb = client["testing"]
mycollection = mydb["store"]

lat = input("Enter the latitude: ")
lon = input("Enter the longitude: ")

records = mycollection.find({'lat': lat,'lng': lon})

for results in records:
    print(results)

