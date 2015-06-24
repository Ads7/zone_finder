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
		dic[variables[0]]=row[0]
		dic[variables[1]]=row[1]
		dic[variables[2]]=row[2]
		distance.append(vincenty((latitude, longitude), (float(row[-2]), float(row[-1]))).meters)
		dictionary.append(dic)

	for i in xrange(0,4):
		selected.append(dictionary[distance.index(min(distance))][variables[0]])
		distance.remove(min(distance))		
	
	return dictionary, selected	


# takes input of a latitude and longitude 
# and returns the corresponding message string 

def subzonefinder(latitude, longitude):
	message = "hello"
	
	query = "SELECT city_id, state_id, name, latitude, longitude FROM cities"
	cur.execute(query)
	citylist = (cur.fetchall()) 
	diccity = []
	distance =[]
	selectedcities = []
	
	for row in citylist:
		dic = {}
		dic["city_id"]=row[0]
		dic["state_id"]=row[1]
		dic["name"]=row[2]
		distance.append(vincenty((latitude, longitude), (float(row[-2]), float(row[-1]))).meters)
		diccity.append(dic)
	
	for i in xrange(0,4):
		selectedcities.append(diccity[distance.index(min(distance))]["city_id"])
		distance.remove(min(distance))
	
	print selectedcities

	variables =["city_id", "state_id", "name"]
	dic, selectedzones = datafinder(query,latitude,longitude,variables)
	
	print selectedzones



	# query = 'SELECT zone_id, city_id, name,latitude, longitude FROM zones WHERE city_id IN (' + ','.join((str(n) for n in selectedcities)) + ')'
	# cur.execute(query)
	# zonelist = (cur.fetchall())
	# 	diczone = []
	# distance =[]
	# selectedzones = []
	# print "<--      -->"

	# for row in zonelist:
	# 	dic = {}
	# 	dic["zone_id"]=row[0]
	# 	dic["city_id"]=row[1]
	# 	dic["name"]=row[2]
	# 	distance.append(vincenty((latitude, longitude), (float(row[-2]), float(row[-1]))).meters)
	# 	diczone.append(dic)

	# for i in xrange(0,4):
	# 	selectedzones.append(diczone[distance.index(min(distance))]["zone_id"])
	# 	distance.remove(min(distance))

	# selectedzones	

	# query = 'SELECT subzone_id, zone_id, name,latitude, longitude FROM subzones WHERE zone_id IN (' + ','.join((str(n) for n in selectedzones)) + ')'
	# cur.execute(query)
	# subzonelist = (cur.fetchall()) 
	# dicsubzone= []
	# distance =[]
	# selectedsubzones = []
	
	# for row in list:
	# 	dic = {}
	# 	dic["city_id"]=row[0]
	# 	dic["state_id"]=row[1]
	# 	dic["name"]=row[2]
	# 	distance.append(vincenty((latitude, longitude), (float(row[-2]), float(row[-1]))).meters)
	# 	diccity.append(dic)
	
	# for i in xrange(0,4):
	# 	selectedcities.append(diccity[distance.index(min(distance))]["city_id"])
	# 	distance.remove(min(distance))



	# message += "subzone" + str(selectedsubzones[0][1])
	return message


def main():
	print subzonefinder(46.5969369687,-120.5267444947)

if __name__ == '__main__':
	main()