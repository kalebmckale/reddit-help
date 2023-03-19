results = [1, 0, "", None, "0", True, False]
results = list(filter(None, results))
print(results)

commands = {
    "h": "help",
    "s": "start",
    "i": "info",
}

print("my nice program")
print("options")
for option, command in commands.items():
    print(f"{option} - {command}")

while True:
    option = input("> ").lower()
    print(commands.get(option, "I didn't understand"))
    if option == "s":
        break
        
def main():
    options = {
        "h": "help",
        "s": "start",
        "i": "info",
    }
    
    print("my nice program")
    print("options")
    for option, command in options.items():
        print(f"{option} - {command}")
    
    while True:
        option = input("> ").lower()
        print(options.get(option, "I didn't understand"))
        if option == "s":
            break
            
from string import ascii_lowercase as alphabet
letters_guessed = ["e", "i", "k", "p", "r", "s"]

def get_available_letters(letters_guessed):
    return "".join(set(alphabet) - set(letters_guessed))
    
def alternate_timeline():
    timeline = range(1, 21)
    for i in timeline:
        print("ba"[(i - 1) % 10 < 5])