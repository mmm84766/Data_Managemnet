import csv
import json

csvfile = open('prediction_data.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("retailer_id","offer_price","quantity","product_id","regular_price","limited")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
