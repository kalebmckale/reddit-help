import time


class Scene:
    def print_pause(self, msg_list):
        for message in msg_list:
            print(message)
            time.sleep(1)

    def _make_prompt(self):
        if not self._options:
            raise NotImplementedError(f"{self.__class__.__name__} hasn't implemented options.")

        prompt = f"please enter {{}} or '{list(self._options)[-1]}': "
        return prompt.format(', '.join(f"'{option}'" for option in list(self._options)[:-1]))

    def make_choice(self):
        prompt = self._make_prompt()
        while (choice := input(prompt)) not in self._options:
            print("you have made an invalid choice, try again")
        self._options[choice]()

class Intro(Scene):
    def __init__(self):
        self._options = None

    def enter(self):
        msg_list = [
            "you are a cat, you are sitting in your cozy home.",
            "suddenly, you hear a noise from the kitchen",
            "you decided to investigate",
        ]
        self.print_pause(msg_list)


class Kitchen(Scene):
    def __init__(self):
        self._options = {
            "attack": self.attack,
            "owner": self.owner,
            "other cat": self.other_cat
        }

    def enter(self):
        msg_list = [
            "you walk into the kitchen and see a rat trying to open the pantry",
            "do you want to attack the mouse, get your owner or get the other cat",
        ]
        self.print_pause(msg_list)
        self.make_choice()

    def attack(self):
        msg_list = [
            "you attack the rat",
            "you hit the rat, it runs away and goes outside",
        ]
        self.print_pause(msg_list)

    def owner(self):
        msg_list = [
            "you run to the bedroom and try and get your owners attention",
            "he is sleeping. do what you must, little kitten",
            "WAKE HIM FROM HIS SLUMBER",
            "you wake him up, he isn't happy but you go to the kitchen and find the rat is already gone",
        ]
        self.print_pause(msg_list)

    def other_cat(self):
        msg_list = [
            "you wake the other cat up, she follows you to the kitchen where she attacks the rat until the rat is badly injured",
            "she drags the rat outside and than leaves it there",
        ]
        self.print_pause(msg_list)


class Bedroom(Scene):
    def __init__(self):
        self._options = None

    def enter(self):
        msg_list = [
            "you go to the bedroom and find the owner now reading his book",
        ]
        self.print_pause(msg_list)


class Game:
    def __init__(self):
        self.scenes = {
            "intro": Intro(),
            "kitchen": Kitchen(),
            "bedroom": Bedroom(),
        }
        self.items = []

    def play(self):
        self.scenes["intro"].enter()
        self.scenes["kitchen"].enter()
        self.scenes["bedroom"].enter()


the_game = Game()
the_game.play()