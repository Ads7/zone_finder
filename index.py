from flask import Flask,render_template, request, redirect, url_for,flash, jsonify 
from googleplaces import GooglePlaces, types, lang
app = Flask(__name__)

# unique abpi key registered to ads71993@gmail.com
YOUR_API_KEY = 'AIzaSyBVWtEz2Ksqvde9hU1UmQur-Q44H3av9O0'
google_places = GooglePlaces(YOUR_API_KEY)

@app.route("/")
def hello():
    ## for parameters passed like name and location /?name=abc&location=abc
    name = request.args.get('name')
    location =  request.args.get('location')
    query_result = google_places.nearby_search(name=name,
        location=location,keyword='chicken',
        radius=20000, types=[types.TYPE_FOOD])

    data = []
    for place in query_result.places:
    	# Returned places from a query are place summaries.
    	data.append(place.name +"......"+place.geo_location+"...."+place.place_id)
    print data
    return data

if __name__ == "__main__":
    app.run()

