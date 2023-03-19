from functools import partial

def adder(y, x):
    return x + y

add_10 = partial(adder, x=10)


PLEASE HELP. Translate method confusion.

HEX_FILTER = ‘’.join([(len(repr(chr(i))) == 3) and chr(i) or ‘.’ for i in range(256)]) 

word = “string”

printable = word.translate(HEX_FILTER)

I seen this in the book Black Hat Python 2nd Edition and I cannot understand the purpose. It’s from a section “building a TCP proxy”. It explains that “we use the *translate* built-in function to substitute the string representation of each character for the corresponding character in the raw string (printable).” What affect does the translate method have on the word variable? It seems like there is no change after running it through the translate method. I also thought that the translate method needs a mapping to translate the characters, but it appears here that the translate method is getting a string as argument. What am I missing? PLEASE HELP.