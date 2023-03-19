from string import (
    ascii_letters,
    whitespace,
    digits,
    punctuation
)
    
vowels = 'aeiouAEIOU'
consonants = ''.join(
    filter(
        lambda c: c not in vowels,
        ascii_letters
    )
)
    
convert = {
    consonants: 'cons',
    vowels: 'vow',
    whitespace: 'space',
    digits: 'num',
    punctuation: 'punc'
}
    
def convert_string(string):
    return ' '.join(
        value for char in string for key, value in convert.items()
        if char in key
    )
    
def remove_endpoints(sequence):
    return (sequence.pop(0), sequence.pop())

#        my_sequence = list(range(6))
#    my_endpoints = remove_endpoints(my_sequence)
