
# This functions accept as an input <tr id="tr_****"> element 
# That is a row in the table of available accomodations

from parser.html import Element

def get_description(el: Element):
    text_el = el.children[2].children[0].children[0].children[0]
    if text_el.tag == "text":
        return text_el.attrs.get("value").replace("\n", " ").strip()
    else:
        return text_el.children[0].attrs.get("value").replace("\n", " ").strip()
    
def get_location(el: Element):
    
    text_el = el.children[3]
    if text_el.children[0].tag == "b":
        text_el = text_el.children[0]

    return text_el.children[0].attrs.get("value") + ", " + text_el.children[2].attrs.get("value")
    
def get_price(el: Element):
    text_el = el.children[8].children[0]
    if text_el.tag == "text":
        return text_el.attrs.get("value").strip()
    elif text_el.tag == "b":
        return (text_el.children[0].attrs.get("value") + el.children[8].children[1].attrs.get("value")).strip()
    else:
        return None
    
def get_link(el: Element):
    return "https://www.ss.com" + el.children[1].children[0].attrs.get("href")
