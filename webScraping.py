from cgitb import html
from http import client
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen


url = 'https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&filters%5Bcountry%5D%5B0%5D=Saudi%20Arabia&q=it'

client = urlopen(url)
html= client.read()
client.close()

soup = bs(html,"html.parser")


classDiv= "css-1gatmva e1v1l3u10"

containers=soup.find_all("div",{"class":classDiv})
Number_offers_page = len(containers)
bs.prettify(containers[0])
titleOffer = containers[0].div.h2.text
print(titleOffer)
locationOffer = containers[0].div.span.text
print(locationOffer)