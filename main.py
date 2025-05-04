from urllib.request import urlopen

url = "https://www.ss.com/lv/real-estate/flats/riga/all/hand_over/"
page = urlopen(url)
html = page.read().decode("utf-8")

print(html)