'''
In this section, we’ll create a metaclass without "type()".
To create a custom metaclass we have to inherit "type" metaclass and override __init__() and __new__().

__new__: It creates a new object and returns it. Before the control goes to __init__(), __new__() is called.

__init__: It initializes the created object.


'''
# Defining a class
class A:
  pass

# Defining our own new method
def new(cls):
  x = object.__new__(cls)
  x.attr = 1
  return x

# override __new__() method
A.__new__ = new


# Making an object and testing
obj = A()
print(obj.attr)

'''
Look at line 22. We are overriding the __new__ method of A with the new method we define above. 
The difference is that __new__ only creates and returns the object and initialization is left for __init__. 
But now after overriding, the __new__ will also do initialization (line 18).
'''
'''
Remember, a class deriving from a metaclass is also a metaclass.
'''
