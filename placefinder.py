from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyBVWtEz2Ksqvde9hU1UmQur-Q44H3av9O0'

google_places = GooglePlaces(YOUR_API_KEY)

# You may prefer to use the text_search API, instead.
query_result = google_places.nearby_search(name='karims',
        location='jama masjid,delhi',keyword='',
        radius=20000, types=[types.TYPE_FOOD])

# if query_result.has_attributions:
#     print query_result.html_attributions

data = []
for place in query_result.places:
    # Returned places from a query are place summaries.
    data.append(place.name)
    data.append(place.geo_location)
    data.append(place.place_id)

print data    

    # # The following method has to make a further API call.
    # place.get_details()
    # # Referencing any of the attributes below, prior to making a call to
    # # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    # print place.details # A dict matching the JSON response from Google.
    # print place.local_phone_number
    # print place.international_phone_number
    # print place.website
    # print place.url

    # # Getting place photos

    # for photo in place.photos:
    #     # 'maxheight' or 'maxwidth' is required
    #     photo.get(maxheight=500, maxwidth=500)
    #     # MIME-type, e.g. 'image/jpeg'
    #     photo.mimetype
    #     # Image URL
    #     photo.url
    #     # Original filename (optional)
    #     photo.filename
    #     # Raw image data
    #     photo.data