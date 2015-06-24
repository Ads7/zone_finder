import urllib2
import json
import time

# lat = 47.6725842440
# lng = -122.3800486926
name = "mcDonald s"
add = "350 Bridge St, Clarkston, WA 99403"

def getlatlng(add):
    add = urllib2.quote(add)
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyDg6pbLVg8xOSg5rus8W0OkgD3fnBIjhcQ" % add
    print geocode_url
    req = urllib2.urlopen(geocode_url)
    jsonResponse = json.loads(req.read())
    lat = (jsonResponse["results"][0]["geometry"]["location"].get("lat")) 
    lng = (jsonResponse["results"][0]["geometry"]["location"].get("lng"))

    return lat,lng

def getlatlngname(add, name):
    lat,lng = getlatlng(add)
    geocode_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
    geocode_url += str(lat)+","+str(lng)
    geocode_url += "&radius=1000&types=food&keyword="
    geocode_url += urllib2.quote(name)
    geocode_url += "&key=AIzaSyDg6pbLVg8xOSg5rus8W0OkgD3fnBIjhcQ"
    req = urllib2.urlopen(geocode_url)
    jsonResponse = json.loads(req.read())
    lat = (jsonResponse["results"][0]["geometry"]["location"].get("lat")) 
    lng = (jsonResponse["results"][0]["geometry"]["location"].get("lng"))
    return lat,lng

