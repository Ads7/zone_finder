from flask import Flask,render_template, request, redirect, url_for,flash, jsonify 
from googleplaces import GooglePlaces, types, lang
import json
from subzonefinder import *
from geopy.distance import vincenty
from datetime import datetime
from untitled import *


app = Flask(__name__)


@app.route("/check/", methods=['GET','POST'])
def checkRestaurant():
	## for parameters passed like name and location /?name=abc&location=abc
	if request.method == 'POST':
		messages =[]
		if request.form.get("lat") and request.form.get("lng"):
			messages = subzonefinder(request.form.get("lat"), request.form.get("lng"))
		elif request.form.get("location"):
			location = request.form.get("location")
			if request.form.get("name"):
				name = request.form.get("name")
				try:
					messages=["Nothing Found"]
					lat,lng = getlatlngname(location, name)
					output = subzonefinder(lat, lng)
					messages = output	

				except Exception as inst:
					messages=["error occured"]			
		
			else:
				lat,lng = getlatlng(location) 
				messages = subzonefinder(lat, lng)
		else:
			messages=["bring more data"]	

		return render_template('form.html', messages = messages ) 

	else:
		return render_template('form.html')
		

if __name__ == "__main__":
	app.run(debug=True)

