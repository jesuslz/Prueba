class MyClass(object):
    def __init__(self, a, b):
        self.a = a 
        self.b = b 
        self.suma(self.a, self.b)
    
    def suma(self, a, b):
        return a + b