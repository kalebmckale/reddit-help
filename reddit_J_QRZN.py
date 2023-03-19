import string

def permute(alph, offset=0):
    return (
       f"{alph[offset:]}"
       f"{alph[:offset]}"
    )

def subst(text, alph, offset=0):
    return (
        "".join(
            dict(
                zip(
                    alph,
                    permute(
                        alph,
                        offset
                    )
                )
            ).get(letter, letter)
            for letter in text
        )
    )

text = "J QRZN"
alph = string.ascii_uppercase
#print(text)
for i in range(26):
    new_text = subst(
        text,
        alph,
        i,
    )
    print(new_text)
