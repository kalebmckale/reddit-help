
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def greet(self):
        print(f"Hello, {self._name}!")

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**kwargs)
        
    def update_age(self, age):
        self._age = age
        
        
class Class:
    def __init__(self, *args, **kwargs):
        self._args = args
        print(f'Class[self: {self}, args: {args}, kwargs: {kwargs}]')
        
    def __new__(cls, *args, **kwargs):
        print(f'Class[cls: {cls}, args: {args}, kwargs: {kwargs}]')
        return super().__new__(cls)
        
    def amethod(self):
        print(self._args)
        
class Subclass(Class):
    def __init__(self, *args, **kwargs):
        self._args = args
        print(f'Subclass[self: {self}, args: {args}, kwargs: {kwargs}]')
        
    def __new__(cls, *args, **kwargs):
        print(f'Subclass[cls: {cls}, args: {args}, kwargs: {kwargs}]')
        return super().__new__(cls, *args, *kwargs)
        
    def amethod(self):
        print(self._args)
