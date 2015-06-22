from flask import Flask,render_template, request, redirect, url_for,flash, jsonify 
from googleplaces import GooglePlaces, types, lang
app = Flask(__name__)

# unique abpi key registered to ads71993@gmail.com
YOUR_API_KEY = 'AIzaSyBVWtEz2Ksqvde9hU1UmQur-Q44H3av9O0'


@app.route("/")
def hello():
	## for parameters passed like name and location /?name=abc&location=abc
	if request.args.get('name'):
		name = request.args.get('name')
	if request.args.get('location'):
		location =  request.args.get('location')
	google_places = GooglePlaces(YOUR_API_KEY)	
	query_result = google_places.nearby_search(name='Kwality Restaurant',
		location='karol bagh , delhi',keyword='chicken',
		radius=20000, types=[types.TYPE_FOOD])
	data = []
	for place in query_result.places:
		print(place.name)
		print(place.geo_location)
		print(place.place_id)
	return str(place.name)+str(place.geo_location)+str(place.place_id)

if __name__ == "__main__":
    app.run()

