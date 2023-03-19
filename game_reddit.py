"""
while running if i type anything random like "dooooeeedooo" .....it ir prints "i don't understand that..." ...but when i anything appropriate after that like "start" or "stop"...it doesn't print anything...just gives me an input section
"""

game_options = (
    "start - to start the car",
    "stop - to stop the car",
    "quit - to exit",
    "help - to display this list"
)

game_output = {
    "start": "Car started...Ready to go!",
    "stop": "Car stopped.",
    "help": "\n".join(game_options),
}

while (command := input("> ").lower()) != "quit":
    try:
        print(game_output[command])
    except KeyError:
        print("I don't understand that option...")
        print(game_output["help"])
