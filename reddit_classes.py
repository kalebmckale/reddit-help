class Foo:
    def __init__(self):
        self.model = 'A'

    def create(self):
        print(f"Model in class Foo {self.model}")
    
class Bar(Foo):
    def __init__(self):
        self._super = Foo()
        self.model = 'B'
        
    def save(self):
        self._super.create()
        print(f"Model in class Bar {self.model}")
        
bar = Bar()
bar.save()

class Foo:
    def __init_subclass__(cls):
	    cls.model = 'A'
        
    @classmethod
    def create(cls):
        print(f"Model in class Foo {cls.model}")
        
class Bar(Foo):
    def __init__(self):
        super().__init__()
        self.model = 'B'
            
    def save(self):
        super().create()
        print(f"Model in class Bar {self.model}")
            
bar = Bar()
bar.save()
