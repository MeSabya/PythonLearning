import time

# Decorator for timing the passed functions
def time_taken(func):

    def wrapper(*args, **kwargs):

        start = time.time()
        resp = func(*args, **kwargs)
        end = time.time()
        return (end - start)

    return wrapper

# Class decorator making use of time_taken decorator to debug class methods
def timeit(cls):

    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, time_taken(val))

    return cls

''' Metaclass feeding created class object to timeit method to get timing
 functionality enabled objects '''
class TimeMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = timeit(obj)
        return obj

''' Base class with metaclass TimeMeta, now all the subclass of this  
will have timing applied '''

class Animal(metaclass=TimeMeta):

    def talk(self):
        time.sleep(1)
        print("Animal talk")


class Cow(Animal):
    def talk(self):
        time.sleep(1)
        print("Moo")

class Dog(Animal):
    def talk(self):
        time.sleep(1)
        print("Bark")


animal = Animal()
cow = Cow()
dog = Dog()

print(animal.talk())
print(cow.talk())
print(dog.talk())