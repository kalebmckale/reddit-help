import itertools as it

GRADE_SCALE = {
    'A': (80, 100),
    'B': (60, 80),
    'C': (40, 60),
    'D': (20, 40),
    'F': (0, 20),
}


def grade_range(grade):
    for ltr, rng in GRADE_SCALE.items():
        if grade in range(*rng):
            return ltr

