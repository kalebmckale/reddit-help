import itertools as it

from enum import Enum
from functools import cached_property, total_ordering


### Support classes ###
class AutoNumberEnum(Enum):
    def __new__(cls, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj
        
    def __str__(self):
        return self._name_.lower()


@total_ordering
class OrderedEnum(AutoNumberEnum):
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        return NotImplemented
 
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.value > other.value
        return NotImplemented


### Armor classes ###
class ArmorType(AutoNumberEnum):
    # Assign properties of armor types here
    HELMET = {'body': 'head'}
    CHESTPLATE = {'body': 'chest'}
    LEGGINGS = {'body': 'legs'}
    BOOTS = {'body': 'feet'}
    
    def __init__(self, stats):
        self._body = stats['body']
        
    def equip(self):
        return self._body


class ArmorClass(OrderedEnum):
    # Assign properties of armor classes here
    LEATHER = {}
    GOLDEN = {}
    CHAINMAIL = {}
    IRON = {}
    DIAMOND = {}
    NETHERITE = {}
    TURTLE = {'only': ArmorType.HELMET}

    def __init__(self, stats):
        self._only = stats.get('only')
            
    def check(self, armor_type):
        return armor_type == self._only if self._only else True


class ArmorItem:
    def __init__(self, armor_class, armor_type):
        if not isinstance(armor_class, ArmorClass):
            raise ValueError(
                "armor_class expected type 'ArmorClass': "
                f"'{armor_class.__class__.__name__}' given")

        self._class = armor_class

        if not isinstance(armor_type, ArmorType):
            raise ValueError(
                "armor_type expected type 'ArmorType': "
                f"'{armor_type.__class__.__name__}' given")

        if not self._class.check(armor_type):
            raise ValueError(
                f"'{self._class}_{armor_type}' is not a possible "
                f"{self.__class__.__name__} instance."
            )

        self._type = armor_type
        
        self._name = f"{self._class}_{self._type}"
        self._value = (self._class.value, self._type.value)

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self._name}: {self._value}>"

    def __str__(self):
        return self._name

    def equip(self):
        return self._type.equip()

    @classmethod
    def from_str(cls, armor_str):
        try:
            return cls(
                *it.starmap(
                    getattr,
                    zip((ArmorClass, ArmorType), armor_str.upper().split("_"))
                )
            )
        except AttributeError as exc:
            raise ValueError(f"{armor_str} is not a valid option: [Error: {exc}]") from None


class ArmorEquipped(Exception):
    pass


class Armor:
    def __init__(self, **kwargs):
        self._head = kwargs.get("head")
        self._chest = kwargs.get("chest")
        self._legs = kwargs.get("legs")
        self._feet = kwargs.get("feet")

    def is_equipped(self, armor_item):
        # Returns the item equipped or None
        return get_attr(self, f"_{armor_item.equip()}")

    def equip(self, armor_item, replace=False):
        if (existing := self.is_equipped(armor_item)) and not replace:
            raise ArmorEquipped(
                f"{armor_item} cannot be equipped because {existing} is equipped "
                f"and replace is set to {replace}."
            )
        set_attr(self, f"_{armor_item.equip()}", armor_item)
        

class Player:
    def __init__(self, name, stats):
        self._name = name
        self._armor = Armor()
        
    def equip_item(self, item, replace=True):
        if isinstance(item, ArmorItem):
            self._armor.equip(armor_item, replace)


        

##### ORIGINAL CODE BELOW #####

#Defining classes
class Enchantment:
    def __init__ (self, id, lvl):
        self.id = id
        self.lvl = lvl

tick = True
user_input = ""

#Functions
def Armor():
    ArmorPiece = ""
    def ArmorIdSearch():
        for ArmorIndex in ArmorItems:
            if user_input.replace("set", "") in ArmorIndex:
                print("Armor set to \"" + user_input.replace("set", "") + "\"")
                ArmorPiece = user_input.replace("set", "")
                print(ArmorPiece)
                return
        print("Unknown item \"" + str(user_input.replace("set", "")) + "\"")
    user_input = ""
    while not user_input == "back":
        user_input = user_input().lower().replace(" ", "")
        if user_input == "back":
            print("\nReturend back to main selection")
        if user_input.count("set") == 1:
            ArmorIdSearch()
        if user_input.count("list") == 1:
            if user_input == "list":
                print(ArmorItems)
            elif user_input.replace("list", "") == "ench":
                print("Enchantments: ")
        if user_input == "cur":
            print(ArmorPiece)
#        elif user_input == "cur" and ArmorPiece == "":
#            print(ArmorPiece)
#            print("No armor provided")

def pend():
    action, item = user_input.split()
    if action == "set":
        try:
            player.equip_item(ArmorItem.from_str(item))
        except ValueError:
            print(f"Unknown item '{item}'")   
    

class Game:
    _OPTIONS = {
        "armor": {
            "help_text": "Opens the armor editor.",
            "action": "open_armor_editor",
        },
        "help": {
            "help_text": "Shows this info.",
            "action": "display_help",
        },
        "exit": {
            "help_text": "Exits the program.",
            "action": "exit",
        }
    }
    def __init__(self):
        self.__class__.update_options()

    @classmethod
    def update_options(cls):
        for option, info in cls._OPTIONS.items():
            try:
                info["action"] = getattr(cls, info["action"])
            except AttributeError:
                print(f"problem with {option}: {info}")
                #del cls._OPTIONS[option]

    @classmethod
    def open_armor_editor(cls):
        return True

    @classmethod
    def display_help(cls):
        output = "\n".join((
            "\nAvailable commands",
            *(f"'{option}' - {info['help_text']}" for option, info in cls._OPTIONS.items())
        ))
        print(output)
        return True

    @classmethod
    def exit(cls):
        print("Inside exit()")
        return False
        
    def process_user_input(self, user_input):
        try:
            return self._OPTIONS[user_input]["action"]()
        except KeyError:
            print(f"'{user_input}' is an unknown option.")
            self.display_help()
        
        
        


#While
def main():
    while tick:
        user_input = user_input().lower().replace(" ", "")
        if user_input == "stop":
            tick = False
        elif user_input == "help":
            print("\nAvailable commands\n\"armor\" - Opens the armor editor\n\"help\" - Shows this info\n\"stop\" - Stops the program")
        elif user_input == "armor":
            print("\nYou have selected the armor editor. Type \"back\" to go back.")
            Armor()
        else:
            print("Unknown command. Type \"help\" to get a list of available commands.")