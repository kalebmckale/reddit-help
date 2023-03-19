from string import ascii_lowercase as ALPH


def alph_rotate(shift=0):
    return f"{ALPH[shift:]}{ALPH[:shift]}"


def alph_gen(key):
    index = -1
    key_length = len(key)
    alph = {char: alph_rotate(ALPH.index(char)) for char in key}
    while True:
        yield alph[key[(index := index + 1) % key_length]]


def encrypt(text, key):
    alph = alph_gen(key.replace(" ", "").lower())
    return "".join(
        next(alph)[ALPH.index(char)]
        if char in ALPH
        else next(alph)[ALPH.index(char.lower())].upper()
        if char.lower() in ALPH
        else char
        for char in text
    )
