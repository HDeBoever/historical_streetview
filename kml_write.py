import simplekml, os, sys


def main(argv):

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

if __name__ == '__main__':
	main(sys.argv)
