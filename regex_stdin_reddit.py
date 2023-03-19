"""
Getting grades from standard input

The text below is an input file and I don't know how to extract these numbers from the standard input and put them into variables so I can work with these numbers.

    Anne Adema____________6.5 5.5 4.5
    Bea de Bruin__________6.7 7.2 7.7
    Chris Cohen___________6.8 7.8 7.3
    Dirk Dirksen__________1.0 5.0 7.7

I need to use the following line of code to make sure that the code can read the standard input and that the formatting isn't screwed.

    import sys
    
    for l in sys.stdin.read().splitlines():
    print(l)

Does anyone know a method of extracting the numbers from the standard input?
"""
from re import compile as compile_

LINE_PATTERN = compile_(r'([A-Za-z ]+)[_]+([0-9]\.[0-9]) ([0-9]\.[0-9]) ([0-9]\.[0-9])')

line = "Anne Adema____________6.5 5.5 4.5"
name, *grades = LINE_PATTERN.findall(line)[0]
grades = [float(grade) for grade in grades]

print(name)
print(grades)

