"""
Singleton can be implemented in various ways , one is overloading the __new__ method and another by
overloading the __call__ method.
"""

class Singleton2:
    pass


a = Singleton2()
b = Singleton2()

print(id(a) == id(b))
print(a, b)