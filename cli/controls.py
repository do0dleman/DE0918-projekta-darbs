from globals import ALL_DISTRICT_NAMES, settings, write_settings

def handle_user_input(user_input: str):
  command = user_input.split()[0]
  args = user_input.split()[1:]

  match command:
    case "help":
      print("q: exit the program\n" \
      "get_max_price: get current max price for housing\n" \
      "set_max_price <int>: set max price four housing\n"
      )
    case "set_max_price":
      settings["max_price_value"] = int(args[0])
      write_settings()
      print("Max price set!\n")
    case "get_max_price":
      print("Max price: " + str(settings["max_price_value"]) + "\n")
    case "get_whitelist_districts":
      if len(settings["district_whitelist"]) == 0:
        print("Whitelist is currently empty!")
      for district_index in settings["district_whitelist"]:
        print(ALL_DISTRICT_NAMES[district_index])
    case "toggle_whitelist":
      settings["is_district_whitelist"] = not settings["is_district_whitelist"]
      if settings["is_district_whitelist"]:
        print("District whitelist is turned on")
      else:
        print("District whitelist is turned off")
    case "get_all_districts":
      for district in ALL_DISTRICT_NAMES:
        print(district)
    case "add_district":
      is_district_found = False
      for index, district  in enumerate(ALL_DISTRICT_NAMES):
        if district.lower() == args[0].lower():
          is_district_found = True
          settings["district_whitelist"].append(index)
          write_settings()
          print("District added to the whitelist\n")     
      if not is_district_found:
        print("District not found!")
    case "rm_district":
      is_district_found = False
      district_index = -1
      for index, district  in enumerate(ALL_DISTRICT_NAMES):
        if district.lower() == args[0].lower():
          is_district_found = True
          district_index = index     
      if not is_district_found:
        print("District not found!")
        return

      try:
        settings["district_whitelist"].remove(district_index)
        write_settings()
        print("District removed from the whitelist")
      except:
        print("District not found in the whitelist")
    case _:
      print("Unknown command, enter help to learn more.\n")  
    