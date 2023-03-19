from string import ascii_letters as alphabet


def generate_table(key):
    return {
        char: f"{alphabet[alphabet.index(char):]}{alphabet[:alphabet.index(char)]}"
        for char in key.lower()
    }


def key_char(key):
    n = 0
    while True:
        yield key[n % len(key)]
        n += 1


def encrypt(plaintext, key):
    keygen = key_char(key)
    return "".join(
        alphabet[
            (alphabet.index(plain_char.lower()) + alphabet.index(next(keygen).lower()))
            % 26
        ]
        if plain_char.lower() in alphabet
        else plain_char
        for plain_char in plaintext
    )
