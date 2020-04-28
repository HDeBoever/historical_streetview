import re, sys, io, requests
import urllib.request
from PIL import Image
from bs4 import BeautifulSoup


def scrape_images_from_given_url(url):

	site = url

	response = requests.get(site)

	soup = BeautifulSoup(response.text, 'html.parser')
	img_tags = soup.find_all('img')

	urls = [img['src'] for img in img_tags]

	print(urls)

	for url in urls:
		try:
			filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
			if 'http' not in url:
				# sometimes an image source can be relative
				# if it is provide the base url which also happens
				# to be the site variable atm.
				url = '{}{}'.format(site, url)

			print(url, filename.group(1))
			print('\n')
			print(filename)
			print('\n')
			print(filename.group(1))
			sys.exit(0)
			urllib.request.urlretrieve(url, filename.group(1))
		except AttributeError as e:
			print(e)

def main(argv):

	# Attempt to scrape images from a given URL; save the images to the curr directory
	scrape_images_from_given_url('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal')

if __name__ == "__main__":
	main(sys.argv)
