from bs4 import BeautifulSoup
import urllib.request
import shutil
import requests
from urllib.parse import urljoin
import sys, os
import time

# Basic source found here: https://pythonprogramming.altervista.org/how-to-download-images-from-the-web-with-python/?doing_wp_cron=1588099753.4233078956604003906250

# Function used to bring raw HTML into the python environment
def make_soup(url):
	req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
	html = urllib.request.urlopen(req)
	return BeautifulSoup(html, 'html.parser')

def get_images(url):

	# Create a directory to store the incoming images into
	dir_name = url.split('/')[2]
	curr_path = os.getcwd()
	relative_path = curr_path + '/' + dir_name
	if not os.path.exists(relative_path):
		os.makedirs(relative_path)

	# Begin process of ientifying and extracting the images
	soup = make_soup(url)
	images = [img for img in soup.findAll('img')]
	print (str(len(images)) + " images found.")
	print('Downloading images to current working directory.')
	image_links = [each.get('src') for each in images]
	for each in image_links:
		print(each)
		try:
			filename = each.strip().split('/')[-1].strip()
			src = urljoin(url, each)
			print('Getting: ' + filename)
			response = requests.get(src, stream = True)
			# delay to avoid corrupted previews
			#time.sleep(1)
			with open(filename, 'wb') as out_file:
				shutil.copyfileobj(response.raw, out_file)
		except:
			print('An error occured. Continuing.')

		# move the image file from the curr_path to the relative_path
		shutil.move(os.getcwd() + '/' + filename, os.getcwd() + '/' + dir_name + '/'+ filename)
	print('Done.')

def main(argv):

	# Scrape images from a given URL; save the images to the a relative path created by manipulating the URL name
	# get_images('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal')
	# get_images('https://www.victoria.ca/EN/main/residents/archives/photo-gallery/140-years-of-victoria-city-hall.html')
	get_images('http://archives.paris.fr/f/photos/mosaique/?&fnbres=40')

if __name__ == '__main__':
	main(sys.argv)
