from re import compile as createRegExPattern
from collections import Counter

word_pattern = createRegExPattern("[A-Za-z]+['-]*[A-Za-z]*")

hyphenated_word_pattern = createRegExPattern(f"{word_pattern}-{word_pattern}")

other_word_pattern = createRegExPattern("[A-Za-z]+'[A-Za-z]{0, 2}")

def most_common_words(text):
    return Counter(word_pattern.findall(text)).most_common()