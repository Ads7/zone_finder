import urllib2
import json
import time

#finds lat long as per address given
def getlatlng(add):
    add = urllib2.quote(add)
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyDg6pbLVg8xOSg5rus8W0OkgD3fnBIjhcQ" % add
    geocode_url
    req = urllib2.urlopen(geocode_url)
    jsonResponse = json.loads(req.read())
    lat = (jsonResponse["results"][0]["geometry"]["location"].get("lat")) 
    lng = (jsonResponse["results"][0]["geometry"]["location"].get("lng"))
    return lat,lng

#finds lat long as per address and name of restaurant given
def getlatlngname(add, name):
    lat,lng = getlatlng(add)
    try:
        geocode_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
        geocode_url += str(lat)+","+str(lng)
        geocode_url += "&radius=2000&types=food&name="
        geocode_url += urllib2.quote(name)
        geocode_url += "&key=AIzaSyDg6pbLVg8xOSg5rus8W0OkgD3fnBIjhcQ"
        geocode_url
        req = urllib2.urlopen(geocode_url)
        jsonResponse = json.loads(req.read())
        lat = (jsonResponse["results"][0]["geometry"]["location"].get("lat")) 
        lng = (jsonResponse["results"][0]["geometry"]["location"].get("lng"))
        return lat,lng
        #name = (jsonResponse["results"][0]["geometry"][3].get("name"))
    except Exception as e:
        try:
            geocode_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
            geocode_url += str(lat)+","+str(lng)
            geocode_url += "&radius=1500&types=food&keyword="
            geocode_url += urllib2.quote(name)
            geocode_url += "&key=AIzaSyDg6pbLVg8xOSg5rus8W0OkgD3fnBIjhcQ"
            geocode_url
            req = urllib2.urlopen(geocode_url)
            jsonResponse = json.loads(req.read())
            lat = (jsonResponse["results"][0]["geometry"]["location"].get("lat")) 
            lng = (jsonResponse["results"][0]["geometry"]["location"].get("lng"))
            # name = (jsonResponse["results"][0]["geometry"][3].get("name"))
            # print name
            return lat,lng
        except Exception as e:
                try:
                    lat,lng = getlatlng(str(name)+str(add))
                    return lat, lng
                except Exception, e:
                    return lat, lng
