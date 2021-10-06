import csv
import requests
import uuid
import json
from datetime import datetime
from datetime import timedelta

#Conncection to Mongodb

def get_database():
    from pymongo import MongoClient
    import pymongo
    conn = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    db = conn['admin']
    coll = db['databasemanagement']
    return coll
dbname = get_database()   
 
#Read data from CSV

with open('retailers.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     
     for row in reader:
      lat = row['lat']
      lon = row['lng']
      api = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
      json_data = requests.get(api, headers={"User-Agent":"PostmanRuntime/7.28.4"})
      json_data = json_data.json()


      for item in json_data['properties']['timeseries']:
          time = item['time']
          date = time[0:10]
          now = datetime.now()
          currentDate = now.date()
          currentDate = currentDate.strftime("%Y-%m-%d")
          base = datetime.today()
          my_list = []
          
       
          for x in range(0, 5):
              next = base + timedelta(days=x)
              next = next.strftime("%Y-%m-%d")
              my_list.append(next[0:10])

          for i in my_list:
           
              if date == i:

                 temperature = item['data']['instant']['details']['air_temperature']

                 try:
                     description_1 = item['data']['next_1_hours']['summary']['symbol_code']
                     precipitation_amount_1 = item['data']['next_1_hours']['details']['precipitation_amount']
                 except:
                     description_1 = "not found"
                     precipitation_amount_1 = "not found"
                 try:
                     description_6 = item['data']['next_6_hours']['summary']['symbol_code']
                     precipitation_amount_6 = item['data']['next_6_hours']['details']['precipitation_amount']
                 except:
                     description_6 = "not found"
                     precipitation_amount_6 = "not found"
                 try:
                     description_12 = item['data']['next_12_hours']['summary']['symbol_code']
                 except:
                     description_12 = "no found"
                   
                    
                 #Inser into DB
                 x = dbname.insert_one(item)
                 
                 
                 
                 print("\n")
                 print("time : ", time)
                 print("\n")

                 print("--------NOW-------")

                 print("Temperature : ", temperature)

                 print("---------After 1 hour----------")
                 print("Precipitation (mm) : ", precipitation_amount_1)
                 print("Description: ", description_1)

                 print("---------After 6 Hours----------")
                 print("Precipitation (mm) : ", precipitation_amount_6)
                 print("Description: ", description_6)

                 print("---------After 12 Hours-------")
                 print("Description: ", description_12)
        
     
