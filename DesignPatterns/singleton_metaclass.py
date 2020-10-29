class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        print("Class name is", cls)
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MySingleton(metaclass=Singleton):
    def foo(self):
        pass

s1 = MySingleton()
s2 = MySingleton()
print(s1)
print(s2)
