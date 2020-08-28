import simplekml, os, sys
import googlemaps
import wikipedia
from datetime import datetime
from googleplaces import GooglePlaces, types, lang

# function to test the access to a google API and the place attributes
def test_google_api():

	f = open("places_api_key.txt", "r")
	api_key = f.read()
	google_places = GooglePlaces(api_key)

	query_result = google_places.nearby_search(
		lat_lng={'lat': 48.407326, 'lng': -123.329773},
		radius=5000,
		types=[types.TYPE_RESTAURANT] or [types.TYPE_CAFE] or [type.TYPE_BAR] or [type.TYPE_CASINO])

	if query_result.has_attributions:
		print(query_result.html_attributions)

	for place in query_result.places:
		place.get_details()
		# print(dir(place))
		print(place.rating)
		print(place.name)

# Given a place name, return the coordinates of that place using google APIs
def get_coords(location):

	# Obtenir la clé API à partir du dossier text
	f = open("geocoding_api_key.txt", "r")
	api_key = f.read()
	f.close()

	gmaps = googlemaps.Client(key = api_key)
	geocode_result = gmaps.geocode(location)
	lat = geocode_result[0]["geometry"]["location"]["lat"]
	lon = geocode_result[0]["geometry"]["location"]["lng"]
	#test - print results
	print(lat,lon)

	# Return a tuple
	return (lat, lon)

# The location arg given to the get_coords function which uses the GeoCode API
# to return the geographic coordinates of the given search term.
def write_to_kml(location, picture):

	# simplekml takes coords in latitude, then longitude format
	path = os.getcwd()

	if not os.path.exists('test_kml_files'):
		os.mkdir('test_kml_files')

	# print(path)

	relative_path = path + "/test_kml_files"
	kml = simplekml.Kml()
	# modify the filename to make it easier to navigate in a linux system
	filename = location.lower().replace(' ', '_')
	file = (filename + '.kml')
	f = open(file, "w")

	latitude, longitude = get_coords(location)

	point = kml.newpoint(name = (location), coords = [(longitude, latitude, 0)])
	picture_path = kml.addfile(path + '/oldphotosinreallife/' + picture)
	point.description = ('<img src="' + picture_path + '" alt="picture" width="500" height="400" align="left" />')
	kml.savekmz(relative_path + '/' + file)


def main(argv):

	# Main is used for testing purposes
	# test_google_api()

	# get_coords('France')
	# get_coords('Tour Eiffel')

	# This call uses a Google Maps API call to associate geographic coordinates to the provided location
	# steps have to be taken to now associate an image with the .kml file

	#### Paris
	# write_to_kml('Tour Eiffel', 'tour_eiffel.jpg')
	# write_to_kml('Opéra Garnier, Paris', 'opéra_garnier.jpg')
	# write_to_kml('Avenue de l\'Opéra, Paris', 'avenue_de_l\'opéra.jpg')
	# write_to_kml('132 rue d\'Alésia, Paris', '132_alésia.jpg')

	### Berlin
	# write_to_kml('Reichstag', 'reichstag.jpg')

	### Victoria BC
	# write_to_kml('1324 Blanshard street, Victoria BC', '1324_blanshard.jpg')


	# testing wikipedia
	print(wikipedia.summary("Berlin"))



if __name__ == '__main__':
	main(sys.argv)
