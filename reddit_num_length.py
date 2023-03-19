"""
Beginner Question: How to stop a loop over a string's index set without triggering a "String index out of range" error?

Edit: Reddit is eliminating the indentations when I post the code, but all of the indentations are correct in the code that I'm running.

I am trying to write an elementary function to count the number of digits in an integer without using the built-in \`len(\*)\` function. The main \`while\` loop of my function keeps running into an index error when the index exceeds the argument's length.

I understand why the error is happening, but I'm not sure how to fix it.

Here is the code I've written (any print statements in the code are just to help me see the function progress as it works, and I've taken out the 'return' statement at the end because the error prevents it from getting there anyways):

\#How many digits in a given number?
"""

def number_length(num):
    i = 0
    while str(num)[i] != None:
        print(f"Digit {i + 1}: {str(num)[i]}")
        i += 1
"""

count = 0
for digit in str(num):
    count += 1
The function prints out the digits in sequential order and then gives me the following error (I've tried structuring the function a few different ways, but I keep running into the same error -- I think there's some built-in that would be useful for fixing this that I don't yet know about).

Traceback (most recent call last):

File "[main.py](https://main.py/)", line 14, in <module>

print(number\_length(66992343228798989798))

File "[main.py](https://main.py/)", line 10, in number\_length

while str(num)\[i\] != None:

IndexError: string index out of range

This is a problem I've run into a few times as I've been completing various exercises -- how do I trigger a function to stop when it reaches the end of a given element's index?
"""