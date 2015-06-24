from flask import Flask,render_template, request, redirect, url_for,flash, jsonify 
from googleplaces import GooglePlaces, types, lang
import json
from subzonefinder import *
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
		message =""
		if request.form.get("lat") and request.form.get("long"):
			message = str(subzonefinder(request.form.get("lat"), request.form.get("long")))
		elif request.form.get("location"):
			if request.form.get("name"):
				name = request.form.get("name")
				location = request.form.get("location")
				if location:
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
							geo_list = []
							for place in query_result.places:
								geo_list.append(place.geo_location)

						lat,log = geo_list[0].values()	
						output = subzonefinder(lat, log)
						message = str(output)

					except Exception as inst:
						message="error occured"			
		
		return render_template('form.html', message = message ) 

	else:
		return render_template('form.html')
		

if __name__ == "__main__":
	app.run(debug=True)

