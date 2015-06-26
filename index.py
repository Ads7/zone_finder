from flask import Flask,render_template, request, redirect, url_for,flash, jsonify 
from googleplaces import GooglePlaces, types, lang
import json
from subzonefinder import *
from geopy.distance import vincenty
from datetime import datetime
from googleapi import *


app = Flask(__name__)

# Render the form on get request and ton Post Request 
# return the details of nearest subzone 
@app.route("/check/", methods=['GET','POST'])
def checkRestaurant():
	if request.method == 'POST':
		messages =[] 	# list to hold all data returned containg 
						# subzone>zone>city>lat>lng details
		result = {}		# dictionary containg all data returned from
						# google api lat>lnt>name
		details = {}
		images=[]					
		if request.form.get("lat") and request.form.get("lng"):
			messages = subzonefinder(request.form.get("lat"), request.form.get("lng"))
		elif request.form.get("location"):
			location = request.form.get("location")
			if request.form.get("name"):
				name = request.form.get("name")
				try:
					messages=["Nothing Found"]
					result = getlatlngname(location, name)
					messages = subzonefinder(result["lat"], result["lng"])
					if result["place_id"]:
						try:
							details = getdetailbyid(result["place_id"])
							# try:
							# 	getphotos(details["photos_id"])
							# except Exception, e:
							# 	print e
						except Exception, e:
							print e
				except Exception as inst:
					messages=["error occured"]			
		
			else:
				result = getlatlng(location) 
				messages = subzonefinder(result["lat"], result["lng"])

		else:
			messages=["bring more data"]	
	
		return render_template('form.html', messages = messages, result= result , details=details, images=images) 

	else:
		return render_template('form.html')
		

if __name__ == "__main__":
	app.run(debug=True)

