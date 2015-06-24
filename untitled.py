import MySQLdb
from geopy.distance import vincenty

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="amandeep93", # your password
                      db="zonefinder") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 


cur.execute("SELECT city_id, state_id, latitude, longitude FROM cities")

# print all the first cell of all the rows
cities=[]
li=[]
citylist = list(cur.fetchall())
for row in  citylist:
    li=[]
    li.append(row[0])
    li.append(abs(vincenty((41.499498, -81.695391), (float(row[-2]), float(row[-1])))).meters)
    cities.append(li)

selectedcities=sorted(cities, key=lambda x: x[1])[:4]
print selectedcities

cur.execute("SELECT zone_id, city_id, latitude, longitude FROM zones")

# print all the first cell of all the rows
zones=[]
li=[]
zonelist = list(cur.fetchall())
for row in zonelist:
    li=[]
    li.append(row[0])
    li.append(abs(vincenty((41.499498, -81.695391), (float(row[-2]), float(row[-1])))).meters)
    zones.append(li)

selectedzones=sorted(zones, key=lambda x: x[1])[:4]

print selectedzones

cur.execute("SELECT subzone_id, zone_id, name, latitude, longitude FROM subzones")

# print all the first cell of all the rows
subzones=[]
li=[]
subzonelist = list(cur.fetchall())
for row in subzonelist:
    li=[]
    li.append(row[0])
    li.append(row[2])
    li.append(abs(vincenty((41.499498, -81.695391), (float(row[-2]), float(row[-1])))).meters)
    subzones.append(li)

selectedsubzones=sorted(subzones, key=lambda x: x[1])[:4]

print selectedsubzones
# newport_ri = (41.49008, -71.312796)
# >>> cleveland_oh = (41.499498, -81.695391)
# >>> print(vincenty(newport_ri, cleveland_oh).miles)
# 538.3904451566326    

    