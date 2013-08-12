from bs4 import BeautifulSoup
from urllib.request import urlopen

url = urlopen("http://sports.yahoo.com/nhl/scoreboard?d=2013-04-01")

content = url.read()

soup = BeautifulSoup(content)





table = soup.find('table')
rows = table.findAll('tr')

for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        text = td.findAll('yspscores')
        for yspscores in td:
            value = str(yspscores)
            print (value)
