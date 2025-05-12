# Housing Alert

Šis projekts ir izveidots, lai sekotu līdzi izīrējamajiem mājokļiem Rīgā, kas publicēti ss.lv. Testēts uz Python 3.12.

## Koda struktūra

* `cli/controls.py` satur CLI komandu realizācijas
* `cli/helpers.py` satur metodes, kas tiek izmantotas ievades formatēšanai un filtrēšanai
* `parser/` satur pielāgotu HTML parsera klasi, kas balstīta uz iebūvēto `html.parser` bibliotēku, kā arī HTML elementu klasi. Vietnes elementi tiek glabāti koka struktūrā, kur katram mezglam var būt neierobežots skaits bērnelementu un dažādi atribūti
* `websraping/utils.py` satur metodes, lai iegūtu konkrētas vērtības no mājokļa tabulas rindu elementiem
* `globals.py` satur globālos konstantus un iestatījumu failu apstrādi
* `main.py` – programmas sākumpunkts. Satur `main_loop`, kas atkārtoti veic ss.lv lapas pieprasījumus, un ievades ciklu. Abi cikli darbojas paralēli.

## Bibliotēkas

notify\_py – v0.3.43

## Funkcionalitāte

* Starpplatformu paziņojumi par jauniem mājokļu sludinājumiem
* Fona pieprasījumi uz ss.lv
* Pieejamie mājokļu filtri:

  * Maksimālās cenas filtrs
  * Atļauto rajonu saraksts (whitelist)
