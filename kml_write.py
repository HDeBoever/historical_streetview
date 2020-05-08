import simplekml, os, sys
# import googlemaps
from datetime import datetime
from googleplaces import GooglePlaces, types, lang


# function to test the access to a google API and the place attributes
def test_google_api():

	f = open("places_api_key.txt", "r")
	api_key = f.read()
	google_places = GooglePlaces(api_key)

	query_result = google_places.nearby_search(
		lat_lng={'lat': 46.1667, 'lng': -1.15},
		radius=5000,
		types=[types.TYPE_RESTAURANT] or [types.TYPE_CAFE] or [type.TYPE_BAR] or [type.TYPE_CASINO])

	if query_result.has_attributions:
		print(query_result.html_attributions)

	for place in query_result.places:
		place.get_details()
		# print(dir(place))
		print(place.rating)
		print(place.name)

def write_to_kml():

	# simplekml takes coords in long/lat format
	path = os.getcwd()

	if not os.path.exists('test_kml_files'):
		os.mkdir('test_kml_files')

	print(path)

	relative_path = path + "/test_kml_files"
	kml = simplekml.Kml()
	file = ('test_kml.txt')
	f = open(file, "w")
	point = kml.newpoint(name = ("test point"), coords = [(0, 0, 0)])
	kml.save(relative_path + '/' + file)


def main(argv):

	# Main is used for testing purposes
	test_google_api()



if __name__ == '__main__':
	main(sys.argv)
