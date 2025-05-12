import threading
from urllib.request import urlopen
import re

from cli.controls import handle_user_input
from globals import QUERY_PERIOD, URL
from cli.helpers import is_passing_user_filter, register_element
from parser.html import HtmlTree
from webscraping.utils import *

viewed_file = open("viewed.txt", "a+")
viewed_list = []

viewed_file.seek(0)

for line in viewed_file.readlines():
  viewed_list.append(line.replace("\n", ""))   

isInit = len(viewed_list) == 0
timer = None

print("Starting up...")

def main_loop():
  global timer, isInit

  page = urlopen(URL)
  html = page.read().decode("utf-8")

  parser = HtmlTree()
  parser.feed(html)

  elements = parser.get_by_tag("tr")
  filtered_elements = list(filter(lambda el: re.search("tr_\d+", el.get_id()) != None, elements))

  for el in filtered_elements:
    el_id = get_id(el)
    if viewed_list.__contains__(el_id):
      continue

    viewed_list.append(el_id)
    viewed_file.write(el_id)
    viewed_file.write("\n")

    if not isInit and is_passing_user_filter(el):
      register_element(el)
  
  isInit = False
  timer = threading.Timer(QUERY_PERIOD, main_loop)
  timer.start()

# loop that checks website for new housing
main_loop()

# loop for handling cli commands
isFirstInput = True
while True:
  input_msg = ""
  if isFirstInput:
    input_msg = "\n(Enter q to exit, help for more) "
  
  user_input = input(input_msg)
  isFirstInput = False

  if user_input == "q":
    timer.cancel()
    viewed_file.close()
    exit(0)
  else:
    handle_user_input(user_input)