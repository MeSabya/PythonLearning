class Foo:
    def __init__(self):
        self.x = 10
    def __get__(self, name):
        print('__get__ called')

    def __getattr__(self,name):
        return name
    def __getattribute__(self, name):
        if name == 'bar':
            raise AttributeError
        return 'getattribute'

f = Foo()
print(f.x)
print(f.baz)
print(f.bar)