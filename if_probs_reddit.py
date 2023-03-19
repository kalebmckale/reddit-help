MOVES = {
    1: "X|_|_\n_|_|_\n | | ",
    2: "_|X|_\n_|_|_\n | | ",
    3: "_|_|X\n_|_|_\n | | ",
    4: "_|_|_\nX|_|_\n | | ",
    5: "_|_|_\n_|X|_\n | | ",
    6: "_|_|_\n_|_|X\n | | ",
    7: "_|_|_\n_|_|_\nX| | ",
    8: "_|_|_\n_|_|_\n |X| ",
    9: "_|_|_\n_|_|_\n | |X",
}

while True:
    try:
        move1 = int(input("Type your number here:  "))
    except ValueError:
        print("\nYou must enter an integer between 1 and 9. Try again.")
        continue
    if move1 > 10:
        print(
            "\nYour number was greater than 9.  Try again with a number that is less than 9."
        )
    else:
        break

print(MOVES[move1])
