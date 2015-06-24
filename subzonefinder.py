import MySQLdb
from geopy.distance import vincenty

db = MySQLdb.connect(host="localhost", # your host, usually localhost
					 user="root", # your username
					  passwd="amandeep93", # your password
					  db="zonefinder") # name of the data base

db = MySQLdb.connect(host="localhost", # your host, usually localhost
user="root", # your username
passwd="amandeep93", # your password
db="zonefinder")

cur = db.cursor() 


def datafinder(query,latitude, longitude,variables):

	cur.execute(query)
	data = (cur.fetchall()) 
	dictionary = []
	distance =[]
	selected = []
	
	for row in data:
		dic = {}
		dic[variables[0]] = row[0]
		dic[variables[1]] = row[1]
		dic[variables[2]] = row[2]
		dist=float(vincenty((latitude, longitude), (float(row[-2]), float(row[-1]))).meters)
		dic["distance"] = dist
		distance.append(dist)
		dictionary.append(dic)

	for i in xrange(0,5):
		selected.append(dictionary[distance.index(min(distance))][variables[0]])
		distance[distance.index(min(distance))]=10000000000000		
	
	return dictionary, selected	


# takes input of a latitude and longitude 
# and returns the corresponding message string 

def subzonefinder(latitude, longitude):
	message = ""
	
	query = "SELECT city_id, state_id, name, latitude, longitude FROM cities"
	variables =["city_id", "state_id", "name"]
	diccity, selectedcities = datafinder(query,latitude,longitude,variables)
 	
 	query = 'SELECT zone_id, city_id, name,latitude, longitude FROM zones WHERE city_id IN (' + ','.join((str(n) for n in selectedcities)) + ')'	
	variables =["zone_id", "city_id", "name"]
	diczone, selectedzones = datafinder(query,latitude,longitude,variables)

	query = 'SELECT subzone_id, zone_id, name,latitude, longitude FROM subzones WHERE zone_id IN (' + ','.join((str(n) for n in selectedzones)) + ')'
	variables =["subzone_id", "zone_id", "name"]
	dicsubzone, selectedsubzones = datafinder(query,latitude,longitude,variables)

	output = []
	for l in selectedsubzones:
		for i in dicsubzone:
			if l == i["subzone_id"]:
				message = {}
				message["latitude"]=str(latitude)
				message["longitude"]= str(longitude)
				message["distance"] = str(i["distance"])
			 	message["subzone"] = str(i["name"])
				for j in diczone:
					if i["zone_id"] == j["zone_id"]:
						message ["zone"] = str(j["name"]) 
						for k in diccity:
							if k["city_id"] == j["city_id"] :
									message["city"]= str(k["name"])
									output.append(message)

	return output