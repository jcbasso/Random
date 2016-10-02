import requests
from bs4 import BeautifulSoup

url = "https://promociones-aereas.com.ar/"
r = requests.get(url)

soup = BeautifulSoup(r.content,"lxml")

links = soup.find_all("a",{"itemprop": "url","rel": "bookmark"})

# for link in links:
# 	print link.get("href")
# 	print link.text
# 	print "\n"
cantidad = 5

for link in links[0:cantidad]:
	print link.get("href")
	print link.text
	print "\n"
