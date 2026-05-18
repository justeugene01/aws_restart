import csv
import copy

myVehicle={
    "vin":"<empty>",
    "make":"<empty>",
    "model":"<empty>",
    "year": 0,
    "range":0,
    "topSpeed":0,
    "zeroSixty":0.0,
    "mileage":0
    }
    
for key,value in myVehicle.items():
    print("{}:{}".format(key,value))
myInventoryList=[]

with open('car_fleet.csv') as csvFile:
    csvReader=csv.reader(csvFile,delimeter=',')
    lineCount=0
    for row in csvReader:
        if lineCount==0:
            print(f'Column names are:{",".join(row)}')
            lineCount+=1
        else:
            print(f'vin:{row[0]} make:{row[1]}, model:{row[2]},year:{row[3]},range:{row[4]},topSpeed:{row[5]},zeroSixty:{row[6]},mileage:{row[7]}')
            