from flask import Flask,render_template, request, redirect, url_for,flash, jsonify 
from googleplaces import GooglePlaces, types, lang
import json
app = Flask(__name__)

# unique abpi key registered to ads71993@gmail.com
YOUR_API_KEY = 'AIzaSyBVWtEz2Ksqvde9hU1UmQur-Q44H3av9O0'


@app.route("/check/", methods=['GET','POST'])
def checkRestaurant():
	## for parameters passed like name and location /?name=abc&location=abc
	if request.method == 'POST':
		message=""
		# res={}
		# res["message"]="error have occurred"
		# res["condition"]="alert alert-danger"
		name = request.form["name"]
		location = request.form["location"]
		google_places = GooglePlaces(YOUR_API_KEY)  
		try:
			query_result = google_places.nearby_search(name=name,
			location=location,keyword='',
			radius=1500, types=[types.TYPE_FOOD])
			if len(query_result.places):
				message = "Success"
				for place in query_result.places:
					print(place.name)
					print(place.geo_location)
			else:
				message="Nothing Found"
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

