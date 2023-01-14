## Defining Descriptor

👉 **A descriptor is an object with any of the following methods (__get__, __set__, or __delete__), intended to be used via dotted-lookup as
if it were a typical attribute of an instance. For an owner-object, obj_instance, with a descriptor object:**

obj_instance.descriptor invokes
descriptor.__get__(self, obj_instance, owner_class) returning a value
This is how all methods and the get on a property work.

obj_instance.descriptor = value invokes
descriptor.__set__(self, obj_instance, value) returning None
This is how the setter on a property works.

del obj_instance.descriptor invokes
descriptor.__delete__(self, obj_instance) returning None
This is how the deleter on a property works.

## Types of descriptor
- A Data Descriptor has a __set__ and/or __delete__.
- A Non-Data-Descriptor has neither __set__ nor __delete__.

## Why do I need the descriptor class

Imaging you have a class like this

```python
class LineItem:
     price = 10.9
     weight = 2.1
     def __init__(self, name, price, weight):
          self.name = name
          self.price = price
          self.weight = weight

item = LineItem("apple", 2.9, 2.1)
item.price = -0.9  # it's price is negative, you need to refund to your customer even you delivered the apple :(
item.weight = -0.8 # negative weight, it doesn't make sense
```

We should validate the weight and price in avoid to assign them a negative number, we can write less code if we use descriptor as a proxy as this

```python
class Quantity(object):
    __index = 0

    def __init__(self):
        self.__index = self.__class__.__index
        self._storage_name = "quantity#{}".format(self.__index)
        self.__class__.__index += 1

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self._storage_name, value)
        else:
           raise ValueError('value should >0')

   def __get__(self, instance, owner):
        return getattr(instance, self._storage_name)
```

then define class LineItem like this:

```python
class LineItem(object):
     weight = Quantity()
     price = Quantity()

     def __init__(self, name, weight, price):
         self.name = name
         self.weight = weight
         self.price = price
```

and we can extend the Quantity class to do more common validating

