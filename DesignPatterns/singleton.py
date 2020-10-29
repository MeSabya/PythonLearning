'''
__new__ is called when creation of object and __init__ is called while initialization is object...
https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
'''
class Logger(object):
    _instance = None

    def __init__(self):
        print("__init__ is called")
    def __new__(cls):
        if cls._instance is None:
            print("Creating the object", type(cls).__name__)
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance     # if __new__ does not return anything, __init__ will not be called

log1 = Logger()
print(log1)

log2 = Logger() # both log1 and log2 are same, irrespective of new object is created or not __init__ will be called
print(log2)
print("Are they same object?", log1 is log2)

log3 = log2
print(log3)


