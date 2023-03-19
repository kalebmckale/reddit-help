LEET = {"A": "4", "E": "3", "I": "1", "O": "0", "Z": "7", "S": "5", "G": "9"}


def make_leet(line):
    return "_".join(
        "".join(LEET.get(char, char) for char in word)
        for word in line.upper().split()
    )
