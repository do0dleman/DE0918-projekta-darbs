import json
import os

URL = "https://www.ss.com/lv/real-estate/flats/riga/all/hand_over/"
QUERY_PERIOD = 60
SETTINGS_FILE = "settings.json"

if not os.path.isfile(SETTINGS_FILE):
  print("Settings file does not exist, generating default one")
  
  with open(SETTINGS_FILE, mode="x", encoding="utf-8") as write_file:
    json.dump({
      "max_price_value": 550,
      "is_district_whitelist": False,
      "district_whitelist": []
    }, write_file)

with open(SETTINGS_FILE, "r") as file:
  settings = json.load(file)

def write_settings():
  with open(SETTINGS_FILE, mode="w", encoding="utf-8") as write_file:
    json.dump(settings, write_file)
