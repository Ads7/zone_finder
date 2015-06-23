from flask import Flask,render_template, request, redirect, url_for,flash, jsonify 
from googleplaces import GooglePlaces, types, lang
import json
import MySQLdb
from geopy.distance import vincenty
from datetime import datetime


app = Flask(__name__)

db = MySQLdb.connect(host="localhost", # your host, usually localhost
					 user="root", # your username
					  passwd="amandeep93", # your password
					  db="zonefinder") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 


# unique abpi key registered to ads71993@gmail.com
YOUR_API_KEY = 'AIzaSyBVWtEz2Ksqvde9hU1UmQur-Q44H3av9O0'


@app.route("/check/", methods=['GET','POST'])
def checkRestaurant():
	## for parameters passed like name and location /?name=abc&location=abc
	if request.method == 'POST':
		name = request.form.get("name")
		location = request.form.get("location")
		google_places = GooglePlaces(YOUR_API_KEY)  
		try:
			# dt = datetime.now()
			# print dt.microsecond
			message="Nothing Found"

			query_result = google_places.nearby_search(name=name,
				location=location,keyword='',
				radius=1000, types=[types.TYPE_FOOD])
			# dt = datetime.now()
			# print dt.microsecond

			if len(query_result.places):
				message = "Success"
				geo_list=[]
				for place in query_result.places:
					geo_list.append(place.geo_location)

				lat,log=geo_list[0].values()
				print lat
				print log		
				cur.execute("SELECT city_id, state_id, latitude, longitude FROM cities")

				# print all the first cell of all the rows
				cities=[]
				li=[]
				citylist = list(cur.fetchall())
				for row in  citylist:
					li=[]
					li.append(row[0])
					li.append(abs(vincenty((lat, log), (float(row[-2]), float(row[-1])))).meters)
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
					li.append(abs(vincenty((lat, log), (float(row[-2]), float(row[-1])))).meters)
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
					li.append(abs(vincenty((lat, log), (float(row[-2]), float(row[-1])))).meters)
					subzones.append(li)

				selectedsubzones=sorted(subzones, key=lambda x: x[1])[:4]
				for subzone in selectedsubzones:
					message += "  "+str(subzone[1])

		except Exception as inst:
			message="error occured"			
		
		data = []
		# print location
		# print name
		# for place in query_result.places:
		# 	print data.append(str(place.name)+str(place.geo_location)+str(place.place_id))
		
		return render_template('form.html', message = message ) 

	else:
		return render_template('form.html')
		

if __name__ == "__main__":
	app.run(debug=True)

