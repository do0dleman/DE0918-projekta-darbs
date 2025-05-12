# Housing Alert

The project is created to track housing in Riga available for rent on ss.lv

## Code structure

- `cli/controls.py` contains cli command implementaions
- `cli/helpers.py` contains methods used to prettify or filter input
- `parser/` contains custom html parser class and html element class based on built-in library `html.parser`
- `websraping/utils.py` contains methods used to get specific value from the housing table row element
- `globals.py` contains global constants and settings file handling
- `main.py` - programm's entry point. Contains main_loop that repeatedly queries the ss.lv page and input loop. Thoose loops run in paralel.

## Libraries

notify_py - v0.3.43

## Functionality

- Cross platform notification on new housing appearance
- Queries ss.lv in background
- Available housing filters:
  - Max price filter
  - District whitelist
