import json
import os

URL = "https://www.ss.com/lv/real-estate/flats/riga/all/hand_over/"
QUERY_PERIOD = 60
SETTINGS_FILE = "settings.json"
ALL_DISTRICT_NAMES = [
"Centrs",
"Āgenskalns",
"Aplokciems",
"Berģi",
"Bieriņi",
"Bolderāja",
"Brekši",
"Čiekurkalns",
"Dārzciems",
"Daugavgrīva",
"Dzegužkalns (Dzirciems)",
"Grīziņkalns",
"Iļģuciems",
"Imanta",
"Jugla",
"Katlakalns",
"Ķengarags",
"Ķīpsala",
"Klīversala",
"Krasta r-ns",
"Latgales priekšpilsēta",
"Mangaļi",
"Mežaparks",
"Mežciems",
"Pļavnieki",
"Purvciems",
"Rumbula",
"Šampēteris-Pleskodāle",
"Sarkandaugava",
"Šķirotava",
"Teika",
"Torņakalns",
"Vecāķi",
"Vecmīlgrāvis",
"Vecrīga",
"Ziepniekkalns",
"Zolitūde",
"VEF",
"Cits",]

ALL_DISTRICT_LINK_NAMES = [
"centre",
"agenskalns",
"aplokciems",
"bergi",
"bierini",
"bolderaya",
"breksi",
"chiekurkalns",
"darzciems",
"daugavgriva",
"dzeguzhkalns",
"grizinkalns",
"ilguciems",
"imanta",
"yugla",
"katlakalns",
"kengarags",
"kipsala",
"kliversala",
"krasta-st-area",
"maskavas-priekshpilseta",
"mangali",
"mezhapark",
"mezhciems",
"plyavnieki",
"purvciems",
"rumbula",
"shampeteris-pleskodale",
"sarkandaugava",
"shkirotava",
"teika",
"tornjakalns",
"vecaki",
"vecmilgravis",
"vecriga",
"ziepniekkalns",
"zolitude",
"vef",
"other",]

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
