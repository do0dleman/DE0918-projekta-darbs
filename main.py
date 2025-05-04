from urllib.request import urlopen
from parser.html import HtmlTree

url = "https://www.ss.com/lv/real-estate/flats/riga/all/hand_over/"
page = urlopen(url)
html = page.read().decode("utf-8")

parser = HtmlTree()
parser.feed(html)
