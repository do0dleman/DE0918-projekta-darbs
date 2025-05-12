import json

URL = "https://www.ss.com/lv/real-estate/flats/riga/all/hand_over/"
QUERY_PERIOD = 60

with open("settings.json", "r") as file:
  settings = json.load(file)

def write_settings():
  with open("settings.json", mode="w", encoding="utf-8") as write_file:
    json.dump(settings, write_file)
