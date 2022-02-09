#!/opt/homebrew/bin/python3

from bs4 import BeautifulSoup
import urllib.request
import re

PYPI_URL = r"https://pypi.org/simple/"

def get_package_names():
	html_page = urllib.request.urlopen(PYPI_URL)
	soup = BeautifulSoup(html_page, "html.parser")
	hyperlinks = soup.findAll('a')
	for hyperlink in hyperlinks:
		href = hyperlink.get("href")
		package_name = re.findall(r'/simple/(.*)/', href)[0]
		yield package_name

with open("os.txt", 'w') as file:
	for package_name in get_packages_list():
		file.write(package_name + "\n")
