from datetime import datetime 
from urllib.request import urlopen
from parser.html import HtmlTree
import re

from webscraping.utils import *

url = "https://www.ss.com/lv/real-estate/flats/riga/all/hand_over/"

QUERY_PERIOD = 60

last_time = 0
print(last_time)
while True:

  if datetime.now().timestamp() - last_time < QUERY_PERIOD:
      continue
  
  last_time = datetime.now().timestamp()

  page = urlopen(url)
  html = page.read().decode("utf-8")

  parser = HtmlTree()
  parser.feed(html)

  elements = parser.get_by_tag("tr")
  filtered_elements = list(filter(lambda el: re.search("tr_\d+", el.get_id()) != None, elements))

  for el in filtered_elements:
      description = get_description(el)
      location = get_location(el)
      price = get_price(el)
      link = get_link(el)

      print("\n------New Housing------")
      print(description)
      print(location)
      print(price)
      print(link)