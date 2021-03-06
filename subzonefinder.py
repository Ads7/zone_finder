import MySQLdb
from geopy.distance import vincenty

db = MySQLdb.connect(host="localhost", # your host, usually localhost
					 user="root", # your username
					  passwd="amandeep93", # your password
					  db="zonefinder") # name of the data base

cur = db.cursor() 

# fetch and return query from MySql db
# with in take as query, latitude, longitude
# and return a list of selected IDs and dictionary
# of variable details
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
		dic["lat"]	= row[-2]
		dic["lng"]	= row[-1]
		distance.append(dist)
		dictionary.append(dic)

	for i in xrange(0,4):
		selected.append(dictionary[distance.index(min(distance))][variables[0]])
		distance[distance.index(min(distance))]=10000000000000		
	
	return dictionary, selected	


# takes input of a latitude and longitude coordinates
# and returns the corresponding message List 
# containing a sorted list of selected subzones
# along with the details of that subzone
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
				message["latitude"]=str(i["lat"])
				message["longitude"]= str(i["lng"])
				message["distance"] = str(i["distance"])
			 	message["subzone"] = str(i["name"])
				for j in diczone:
					if i["zone_id"] == j["zone_id"]:
						message ["zone"] = str(j["name"]) 
						for k in diccity:
							if k["city_id"] == j["city_id"] :
									message["city"]= str(k["name"])
									output.append(message)
	messages=output
	# messages=[]
	# start = float(output[0]["distance"])
	# for message in output:
	# 	if 	((float(message["distance"])-start)/start)*100 < 40:
	# 		messages.append(message)
	return messages