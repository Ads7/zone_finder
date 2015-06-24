import googlemaps
import urllib2
import pprint
import json

# add = "Buckingham Palace, London, SW1A 1AA"
# add = urllib2.quote(add)
# geocode_url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false&region=uk" % add
# print geocode_url
# req = urllib2.urlopen(geocode_url)
# jsonResponse = json.loads(req.read())
# pprint.pprint(jsonResponse) 

# Replace the API key below with a valid API key.
gmaps = googlemaps.Client(key='AIzaSyDg6pbLVg8xOSg5rus8W0OkgD3fnBIjhcQ')

# Geocoding and address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

lat=geocode_result[0]["geometry"]["location"].get("lat")
lng=geocode_result[0]["geometry"]["location"].get("lng")
