"""
need help with one of my first programs! 😥

hi! im completely new to programming and started learning python a few hours ago. i was trying to practice my skills by trying to make some simple programs and ran into a problem.

This is my code to make a 2d list to store some info for a few students and print it later.

stud_info = [ ]
record = ['', '', '', '']

for n in range(0, 2): 
    stud_info.append([ ])
    record[0] = input("Enter the student ID: ")
    record[1] = input("Enter the student's name: ") 
    record[2] = input("Enter the student's DOB: ") 
    record[3] = input("Enter the student's contact number: ")
    stud_info[n] = record

print(stud_info)

however, upon entering values a1-4 and b1-4 to test it, it returns the second set of values twice!
how can i fix this?
"""
# stud_info = [ ]
# record = ['', '', '', '']

# for n in range(0, 2):
#    stud_info.append([ ])
#    record[0] = input("Enter the student ID: ")
#    record[1] = input("Enter the student's name: ")
#    record[2] = input("Enter the student's DOB: ")
#    record[3] = input("Enter the student's contact number: ")
#    stud_info[n] = record

# print(stud_info)
from dateutil.parser import parse as parse_date, ParserError as DateParserError

from datetime import datetime
from datatest import validate, ValidationError

from re import compile as createRegExPattern
import itertools as it


NUM_STUDENTS = 2
FIELDS_PROMPTS = {
    "id": "Enter the student ID: ",
    "name": "Enter the student's name: ",
    "dob": "Enter the student's DOB: ",
    "phone": "Enter the student's contact number: ",
}
# DATE_FORMATS = [
#    f"{sep}".join(permutation)
#    for permutation, sep in it.product(
#        it.permutations(("%Y", "%m", "%d")),
#        "-/.",
#    )
# ]
DATE_FORMATS = (
    "%d %B %Y",
    "%b %d, %Y",
    *(
        f"{sep}".join(f"%{char}" for char in permutation)
        for permutation in it.permutations("Ymd")
        for sep in "-/."
    ),
)
VALIDATION_ERRORS = {
    "id": "Enter the student ID: ",
    "name": "Enter the student's name: ",
    "dob": "Enter the student's DOB: ",
    "phone": "Enter the student's contact number: ",
}
PHONE_PATTERNS = (
    r"^(\(\d{3}\)) (\d{3})-(\d{4})$",
    r"^(?:\+?1-)?(\d{3})-(\d{3})-(\d{4})$",
    r"^(\d{3})/(\d{3})[.-](\d{4})$",
    r"^(?:\+?1\.)?(\d{3})\.(\d{3})\.(\d{4})$",
    r"^(\d{3}) (\d{3}) (\d{4})$",
)


class InputValidationError(Exception):
    pass


def strftime_format(format):
    def requirement(value):
        try:
            datetime.strptime(value, format)
        except ValueError:
            return False
        return True

    requirement.__doc__ = f"should use date format {format}"
    return requirement


def is_int(string):
    return int


def is_date(string):
    return any(strftime_format(format)(string) for format in DATE_FORMATS)


def is_phone(string):
    return any(createRegExPattern(pattern).search(string) for pattern in PHONE_PATTERNS)


REQUIREMENTS = {
    "id": is_int,
    "name": str,
    "dob": is_date,
    "phone": is_phone,
}

# data = ['2020-02-29', '03-17-2021', '2021-02-29', '2021-04-01']
# try:
#    validate(data, requirement=is_date)
# except ValidationError as exc:
#    print(f'caught exception: {exc}')


class Student:
    def __init__(self, id, name, dob, phone):
        self._id = id
        self._name = name
        self._dob = dob
        self._phone = phone

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self._id}, name={self._name}, dob={self._dob}, phone={self._phone})"
        )

    @staticmethod
    def format_input(field, user_input):
        if field == "dob":
            return parse_date(user_input).strftime("%Y-%m-%d")
        if field == "phone":
            return list(
                filter(
                    None,
                    (
                        createRegExPattern(pattern).findall(user_input)
                        for pattern in PHONE_PATTERNS
                    ),
                )
            )
        return user_input

    @staticmethod
    def validate_input(field, user_input):
        try:
            validate(user_input, requirement=REQUIREMENTS[field])
        except ValidationError as exc:
            raise InputValidationError(exc) from None
        return user_input

    @classmethod
    def from_input(cls):
        student_params = dict.fromkeys(FIELDS_PROMPTS)
        for field, prompt in FIELDS_PROMPTS.items():
            while True:
                try:
                    value = cls.validate_input(field, user_input := input(prompt))
                except (ValueError, InputValidationError):
                    print(f"Invalid input or input failed validation: '{user_input}'.")
                else:
                    student_params[field] = cls.format_input(field, value)
                    break
        return cls(**student_params)


# roster = [Student.from_input() for _ in range(NUM_STUDENTS)]
