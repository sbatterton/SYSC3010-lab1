#!/usr/bin/env python3
import sqlite3

dbconnect = sqlite3.connect("/home/pi/Documents/SYSC 3010/Labs/Lab 3/mydatabase.db")

cursor = dbconnect.cursor()

sql = "CREATE TABLE `sensors` (`sensorID` INTEGER PRIMARY KEY AUTOINCREMENT, `type`	TEXT, `zone` TEXT);"

cursor.execute(sql)

dbconnect.commit()

sensorList = [("door", "kitchen"), ("temperature", "kitchen"), ("door", "garage"), ("motion", "garage"), ("temperature", "garage")]

for sensor in sensorList:
    sql = "INSERT INTO sensors (type, zone) values('"+ sensor[0] +"', '"+ sensor[1] +"');"
    cursor.execute(sql)
    dbconnect.commit()

sql = "select * from sensors where sensors.zone LIKE 'garage'"

cursor.execute(sql)

for r in cursor:
    print("SensorID: " + str(r[0]), "Type: " + str(r[1]),"Zone: " + str(r[2]))
