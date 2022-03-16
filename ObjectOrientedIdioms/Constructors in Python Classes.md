# Constructors in Python Classes

✔ The __new__() method creates a new instance.

✔ The __init__() method initialises that instance.

Obviously, we should create an instance before initialising it. So the __init__() method is called after the __new__() method. Let’s look at an example:

```python
class Student:
    def __new__(cls, *args, **kwargs):
        print("Running __new__() method.")
        instance = object.__new__(cls)
        return instance

    def __init__(self, first_name, last_name):
        print("Running __init__() method.")
        self.first_name = first_name
        self.last_name = last_name

s = Student("Yang", "Zhou")
print(s.last_name)

# Running __new__() method.
# Running __init__() method.
# Zhou
```
The above results show how the s=Student("Yang","Zhou") works:

- A new instance was created by __new__() method firstly.
- Then parameters of this instance were initialised by __init__() method.

## Dive Into The __new__( ) Method

*The __new__() is a static method (special-cased so we need not declare it as such) of a class to create instances. The first parameter is always the cls representing the class itself. Remaining parameters are those needed for the constructor. The return value should be a instance of this class.*

👉 **What will happen when we dont define __new__()**

If we don’t want to customize the __new__() method, there is no need to state it explicitly in our classes. Because Python has already helped us define it in **object**, where all Python classes inherited from.

```python
class Singleton_Student(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        print("Running __new__() method.")
        if not Singleton_Student._instance:
            Singleton_Student._instance = object.__new__(cls)
        return Singleton_Student._instance

    def __init__(self, first_name, last_name):
        print("Running __init__() method.")
        self.first_name = first_name
        self.last_name = last_name

s1 = Singleton_Student("Yang", "Zhou")
s2 = Singleton_Student("Elon", "Musk")

print(s1)
print(s2)
print(s1 == s2)
print(s1.last_name)
print(s2.last_name)

# Running __new__() method.
# Running __init__() method.
# Running __new__() method.
# Running __init__() method.
# <__main__.Singleton_Student object at 0x7ff1e5a53198>
# <__main__.Singleton_Student object at 0x7ff1e5a53198>
# True
# Musk
# Musk
```
👉 **The s1 and s2 are the same instance.**

### More Tips to Use The Constructor Correctly

1. __init__() method must return None , otherwise a TypeError will be raised.
2. If the parent class has defined __init__() method, we should using super().__init__() to explicitly call it in subclasses’ __init__() method to ensure correct initialization.
3. If __new__() method does not return an instance of the class, then the __init__()method will not be invoked.

```python
class Student(object):

    def __new__(cls, *args, **kwargs):
        print("Running __new__() method.")
        return None

    def __init__(self, first_name, last_name):
        print("Running __init__() method.")
        self.first_name = first_name
        self.last_name = last_name


s1 = Student("Yang", "Zhou")
print(s1.last_name)

# Running __new__() method.
# AttributeError: 'NoneType' object has no attribute 'last_name'
```










