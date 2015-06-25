import urllib2
import json
import time

API_KEY = "&key=AIzaSyDg6pbLVg8xOSg5rus8W0OkgD3fnBIjhcQ"

#Takes in Input as address of the place 
# and return back with lat, lng, name 
def getlatlng(add):
    add = urllib2.quote(add)
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyDg6pbLVg8xOSg5rus8W0OkgD3fnBIjhcQ" % add
    geocode_url
    result={}
    try:
        req = urllib2.urlopen(geocode_url)
        jsonResponse = json.loads(req.read())
        result["lat"] = jsonResponse["results"][0]["geometry"]["location"]["lat"]
        result["lng"] = jsonResponse["results"][0]["geometry"]["location"]["lng"]
        result["name"] = jsonResponse["results"][0]["formatted_address"]
        result["types"] = name = jsonResponse["results"][0]["types"]
    except Exception as e:
        print e
    return result

# Takes in Input as address and name of the place 
# and return back with lat, lng, name 
def getlatlngname(add, name):
    result = getlatlng(add)
    lat = result["lat"]
    lng = result["lng"]
    RESPONSE =["ZERO_RESULTS","INVALID_REQUEST"]
    geocode_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
    geocode_url += str(lat)+","+str(lng)+"&radius=3000&types=food&"
    try:
        url = "name="
        url += urllib2.quote(name)
        url += "&keyword="
        url += urllib2.quote(name)
        url += API_KEY
        req = urllib2.urlopen(geocode_url+url)
        print geocode_url+url
        jsonResponse = json.loads(req.read())
        if jsonResponse["status"] not in RESPONSE:
            if len(jsonResponse["results"]) == 1:
                result["name"] = jsonResponse["results"][0]["name"]
                result["lat"] = jsonResponse["results"][0]["geometry"]["location"]["lat"]
                result["lng"] = jsonResponse["results"][0]["geometry"]["location"]["lng"]
            # else:
            #   url = "name="
            #   url += urllib2.quote(name)
            #   url = "&keyword="
            #   url += urllib2.quote(name)
            #   url += "&rankby=distance"
            #   url += API_KEY
            #   req = urllib2.urlopen(geocode_url+url)
            #   result["name"] = jsonResponse["results"][0]["name"]
            #   result["lat"] = jsonResponse["results"][0]["geometry"]["location"]["lat"]
            #   result["lng"] = jsonResponse["results"][0]["geometry"]["location"]["lng"]
            #   print result
    except Exception, e:
        return result

    return result   
          

# def main():
#   name = "karims"
#   add="jama masjid delhi"
#   getlatlngname(add, name)


# if __name__ == "__main__":
#   main()