from notifypy import Notify
from webscraping.utils import *
from globals import ALL_DISTRICT_LINK_NAMES, settings

def is_passing_user_filter(el: Element):
    price = get_price(el)
    price_numeric = int(price.split(" ")[0].replace(",", ""))
    
    if price_numeric > settings["max_price_value"]:
        return False
    
    district = get_district(el)
    district_index = ALL_DISTRICT_LINK_NAMES.index(district)

    if district_index not in settings["district_whitelist"] and settings["is_district_whitelist"]:
        return False

    return True

def register_element(el: Element):
    description = get_description(el)
    location = get_location(el)
    price = get_price(el)
    link = get_link(el)

    print("\n-----------------------------New Housing------------------------------", flush=True)
    print(description, flush=True)

    delimeter = ""
    length = 70 - len(location) - len(price)
    delimeter = delimeter.ljust(length)
    print(location + delimeter + price, flush=True)
    print(link, flush=True)

    notification = Notify()
    notification.application_name = "Housing Alert"
    notification.title = "New Housing: " + price
    notification.message = description
    notification.send()