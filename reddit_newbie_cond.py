"""
I am trying to use Conditional statement but unable to execute it. Please Help. How to resolve this issue??

Hello, I am a newbie in Python and trying to create a conditional statement using if, elif and for.
"""


class D:
    def __init__(self):
        self._val = None
        
    def set(self, val):
        self._val = val

a = 17.2
d = D()


if a == 17.2:
    for c in [10, 24, 38, 52, 66]:
        print(c)
        if c == 10:
            print("d.set(5.0)")
            d.set(5.0)
        elif c == 24:
            print("d.set(6.0)")
            d.set(6.0)
        elif c == 38:
            print("d.set(8.0)")
            d.set(8.0)
        elif c == 52:
            print("d.set(10.0)")
            d.set(10.0)
        elif c == 66:
            print("d.set(16.0)")
            d.set(16.0)
        else:
            print("out of range")

"""
my issue is, whenever I am trying to execute, with a =17.2 and b=10, I am getting 16 as an input instead of 5. Note: a,b,c and d are already defined
"""
''