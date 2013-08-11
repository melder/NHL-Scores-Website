from bs4 import BeautifulSoup
from urllib.request import urlopen

url = urlopen("http://sports.yahoo.com/nhl/scoreboard?d=2013-04-01")

content = url.read()


soup = BeautifulSoup(content)

print (soup.prettify())
