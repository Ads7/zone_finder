import urllib2
import json
import time
from PIL import Image
import requests
# from PIL import Image
from io import BytesIO


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
		result["add"] = jsonResponse["results"][0]["formatted_address"]
		#result["types"] = name = jsonResponse["results"][0]["types"]
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
	geocode_url += str(lat)+","+str(lng)+"&types=food&"
	try:
		url = "name="
		url += urllib2.quote(name)
		url += "&rankby=distance"
		url += "&keyword="
		url += urllib2.quote(name)
		url += API_KEY
		req = urllib2.urlopen(geocode_url+url)
		jsonResponse = json.loads(req.read())
		if jsonResponse["status"] not in RESPONSE:
			result["name"] = jsonResponse["results"][0]["name"]
			result["lat"] = jsonResponse["results"][0]["geometry"]["location"]["lat"]
			result["lng"] = jsonResponse["results"][0]["geometry"]["location"]["lng"]
			result["place_id"] = jsonResponse["results"][0]["place_id"]
			geocode_url+url
	except Exception, e:
		url = "name="
		url += urllib2.quote(name)
		url = "&keyword="
		url += urllib2.quote(name)
		url += "&radius=3000"
		url += API_KEY
		try:
			req = urllib2.urlopen(geocode_url+url)
			jsonResponse = json.loads(req.read())
			if jsonResponse["status"] not in RESPONSE:
				result["name"] = jsonResponse["results"][0]["name"]
				result["lat"] = jsonResponse["results"][0]["geometry"]["location"]["lat"]
				result["lng"] = jsonResponse["results"][0]["geometry"]["location"]["lng"]
				result["place_id"] = jsonResponse["results"][0]["place_id"]
				result["reference"] = jsonResponse["results"][0]["id"]
				geocode_url+url
		except Exception, e:
				return result
			  #print result
	return result   

# returns the details about a place from its name 
# and address		  
def getdetailbyid(_id):
	placeid_url = "https://maps.googleapis.com/maps/api/place/details/json?placeid="
	placeid_url += _id+API_KEY
	placeid_url
	result = {}
	result["place_id"]=_id
	try:
		req = urllib2.urlopen(placeid_url)
		jsonResponse = json.loads(req.read())
		jsonResponse
		if jsonResponse["status"] == "OK":
			result["international_phone_number"]=jsonResponse["result"]["international_phone_number"]
			result["rating"] = jsonResponse["result"]["rating"]
			result["weekday_text"] = jsonResponse["result"]["opening_hours"]["weekday_text"]
			photosref=[]
			for i in jsonResponse["result"]["photos"]:
				photosref.append(i["photo_reference"])
			result["photos_id"]=photosref
			reviewsref=[]
			for i in jsonResponse["result"]["reviews"]:
				if len(i["text"]) > 5:
					reviewsref.append(i["text"])
			result["reviews"] = reviewsref

	except Exception, e:
		print e
	return result

# returns all images of the resturant if present	
def getphotos(photos_id):
	photos_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="
	images=[]
	for i in photos_id:
		try:
			url = i
			url += API_KEY
			response = requests.get(photos_url+url)
			img = Image.open(BytesIO(response.content))
			img.show()
			#img.show()
			images.append(img)
		except Exception, e:
			print e
			continue
	return images		


# def main():
#   name = "McDonald's"
#   add = "350 Bridge St, Clarkston, WA 99403"
#   result = getlatlngname(add, name)
#   if (result["place_id"]):
#   	result = getdetailbyid(result["place_id"])
#   	getphotos(result["photos_id"])
#   else:
#   	print "no id found"	



# if __name__ == "__main__":
#   main()