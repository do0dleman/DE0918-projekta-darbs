from globals import settings, write_settings

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
    case _:
      print("Unknown command, enter help to learn more.\n")  
    