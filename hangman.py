from string import ascii_lowercase

secret = set(word := input("Input the secret word for this hangman game! ").lower())
while not all(char in ascii_lowercase for char in secret):
    print(f"'{word}' is not a valid secret word!")
    secret = set(word := input("Input the secret word for this hangman game! ").lower())

MAX_ATTEMPTS = 5

guesses = set()
num_attempt = 0

while num_attempt < MAX_ATTEMPTS:
    print(" ".join(char if char in guesses else "_" for char in word))
    while (letter := input("\nGuess a letter! ").lower()) not in ascii_lowercase:
        print(f"{letter} is not a valid letter!")
    if letter in guesses:
        print(f"You've already guessed {letter}!")
    guesses.add(letter)
    if letter in secret:
        print("Correct!")
    else:
        print(f"Nope.. you have {MAX_ATTEMPTS - num_attempt} more attempts!")
        num_attempt += 1
    if not secret - guesses:
        print(f'Congradz! You won! The word was "{word}".')
        break
else:
    print(f'GAME OVER!!!!! The word was "{word}".')
