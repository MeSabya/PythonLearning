# Implement the Singleton Pattern by Python

Unfortunately, Python doesn’t have access modifiers like public or private. Does it mean that we can’t control the constructors of Python classes?
In fact, Python gives us more flexibility to modify the constructors of classes. We can implement the singleton pattern more easily in Python. The key is the __new__() method. A common template to implement it is as follows:

```python
class Singleton_Genius(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Singleton_Genius.__instance:
            Singleton_Genius.__instance = object.__new__(cls)
        return Singleton_Genius.__instance

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

s1 = Singleton_Genius("Yang", "Zhou")
s2 = Singleton_Genius("Elon", "Musk")

print(s1)
# <__main__.Singleton_Genius object at 0x7fec946b1760>
print(s2)
# <__main__.Singleton_Genius object at 0x7fec946b1760>
print(s1 == s2)
# True
print(s1.last_name)
# Musk
print(s2.last_name)
# Musk
```

## Avoid the Singleton Classes in Python
As a strictly object-oriented programming language, everything in Java must be a class. However, Python is a multi-paradigm programming language. We don’t have to make everything to be classes. A singleton is not necessarily to be a class as well.
In the Python official documents, there is an answer for the most asked question, “how do I share global variables across modules?”.

[how do I share global variables across modules](https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules)
