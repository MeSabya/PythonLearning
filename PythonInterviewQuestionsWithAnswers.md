## How to use a custom object as a key in a dictionary in Python

DEFINE  ```__hash__() AND __eq__() ``` METHODS FOR A CUSTOM CLASS TO USE A CUSTOM OBJECT AS A KEY IN A DICTIONARY
Define ```__hash__(self) and __eq__(self, other)``` for a custom class. 
Two objects for which ```__hash__(self)``` returns the same value and ```__eq__(self, other)``` evaluates to True will be recognized as the same key. 
Note that ```__eq__(self, other)``` will not be evaluated if ```__hash__(self)``` does not match any keys in the dictionary.

In most cases, the hash function should return the same integer for obj1 and obj2 if and only if the two objects have all the same attribute values, while __eq__(self, other) should return True if and only if self and other have exactly the same attribute values.

```python
class C:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def __hash__(self):
        return hash((self.a1, self.a2))
get a tuple's hash


    def __eq__(self, other):
        return (self.a1, self.a2) == (other.a1, other.a2)

object_a = C("a", 1)
object_b = C("a", 1)
object_c = C("b", 2)

a_dictionary = {object_a : 3, object_b : 4, object_c : 5}

print(a_dictionary[object_a])
```

## Weak references 

The reference count usually works as such: each time you create a reference to an object, it is increased by one, and whenever you delete a reference, it is decreased by one.

Weak references allow you to create references to an object that will not increase the reference count.

The reference count is used by python's Garbage Collector when it runs: any object whose reference count is 0 will be garbage collected.

A primary use for weak references is to implement caches or mappings holding large objects, where it’s desired that a large object not be kept alive solely because it appears in a cache or mapping.

👉 **For example**, 
if you have a number of large binary image objects, you may wish to associate a name with each. If you used a Python dictionary to map names to images, or images to names, the image objects would remain alive just because they appeared as values or keys in the dictionaries. The WeakKeyDictionary and WeakValueDictionary classes supplied by the weakref module are an alternative, using weak references to construct mappings that don’t keep objects alive solely because they appear in the mapping objects. If, for example, an image object is a value in a WeakValueDictionary, then when the last remaining references to that image object are the weak references held by weak mappings, garbage collection can reclaim the object, and its corresponding entries in weak mappings are simply deleted.

To understand the above statement , understand the code snippet below:

👉 **Here is the example comparing dict and WeakValueDictionary:**

```python 
class C: pass
ci=C()
print(ci)

wvd = weakref.WeakValueDictionary({'key' : ci})
print(dict(wvd), len(wvd)) #1
del ci
print(dict(wvd), len(wvd)) #0

ci2=C()
d=dict()
d['key']=ci2
print(d, len(d))
del ci2
print(d, len(d))
```

And here is the output:

```yaml
<__main__.C object at 0x00000213775A1E10>
{'key': <__main__.C object at 0x00000213775A1E10>} 1
{} 0
{'key': <__main__.C object at 0x0000021306B0E588>} 1
{'key': <__main__.C object at 0x0000021306B0E588>} 1
```

## How to list all functions in a Python module?

##### 1. Using dir() to get functions in a module.
##### 2. Using __all__ to get functions in a module
##### 3. Using inspect to get functions in a module

## What does built-in class attribute __dict__ do in Python?
This is the dictionary containing the module’s symbol table.

```python
object.__dict__
```

```python
The following code shows how __dict__ works

class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var

foo = MyClass(2)
bar = MyClass(3)

print MyClass.__dict__
print foo.__dict__
print bar.__dict__
```



## Reflection in Python?

https://www.geeksforgeeks.org/reflection-in-python/
Reflection refers to the ability for code to be able to examine attributes about objects that might be passed as parameters to a function.
Reflection-enabling functions include  **type(), isinstance(), callable(), dir() and getattr().**


### How do I check if an object is an instance of a given class or of a subclass of it?

## Difference between type() and isinstance()?
One major difference is isinstance() supports inheritance while type does not support it.

Example:

```python 
# python code to show isinstance() support
# inheritance
class MyDict(dict):
	"""A normal dict, that is always created with an "initial" key"""

	def __init__(self):
		self["initial"] = "some data"


d = MyDict()
print(isinstance(d, MyDict))
print(isinstance(d, dict))

d = dict()
print(isinstance(d, MyDict))
print(isinstance(d, dict))
```



## why we need class method in python?
Class methods are typically useful when we need to access the class itself — for example, when we want to create a factory method, that is a method that creates instances of the class. In other words, classmethods can serve as alternative constructors.

```python

class Employee:
    NO_OF_EMPLOYEES = 0
  
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.increment_employees()
    def give_raise(self, amount):
        self.salary += amount
    @classmethod
    def employee_from_full_name(cls, full_name, salary):
        split_name = full_name.split(' ')
        first_name = split_name[0]
        last_name = split_name[1]
        return cls(first_name, last_name, salary)
    @classmethod
    def increment_employees(cls):
        cls.NO_OF_EMPLOYEES += 1
    @staticmethod
    def get_employee_legal_obligations_txt():
        legal_obligations = """
        1. An employee must complete 8 hours per working day
        2. ...
        """
        return legal_obligations
```

## What does the "yield" keyword do in Python?

**The yield keyword is reduced to two simple facts:**

- If the compiler detects the yield keyword anywhere inside a function, that function no longer returns via the return statement. Instead, it immediately returns a 
  lazy "pending list" object called a generator

- A generator is iterable. What is an iterable? It's anything like a list or set or range or dict-view, with a built-in protocol for visiting each element in a certain   order.

- Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly:

Original version:

```python
def some_function():
    for i in xrange(4):
        yield i

for i in some_function():
    print i
```

👉 This is basically what the Python interpreter does with the above code:

```python
class it:
    def __init__(self):
        # Start at -1 so that we get 0 when we add 1 below.
        self.count = -1

    # The __iter__ method will be called once by the 'for' loop.
    # The rest of the magic happens on the object returned by this method.
    # In this case it is the object itself.
    def __iter__(self):
        return self

    # The next method will be called repeatedly by the 'for' loop
    # until it raises StopIteration.
    def next(self):
        self.count += 1
        if self.count < 4:
            return self.count
        else:
            # A StopIteration exception is raised
            # to signal that the iterator is done.
            # This is caught implicitly by the 'for' loop.
            raise StopIteration

def some_func():
    return it()

for i in some_func():
    print i

```
For more insight as to what's happening behind the scenes, the for loop can be rewritten to this:

```python
iterator = some_func()
try:
    while 1:
        print iterator.next()
except StopIteration:
    pass

```

## References:
https://github.com/learning-zone/python-interview-questions

## How varibales are passed in Python, Is it pass by value or pass by reference ?

Python's variable passing style as call-by-object:

Objects are allocated on the heap and pointers to them can be passed around anywhere.

When you make an assignment such as x = 1000, a dictionary entry is created that maps the string "x" in the current namespace to a pointer to the integer object containing one thousand.

When you update "x" with x = 2000, a new integer object is created and the dictionary is updated to point at the new object. The old one thousand object is unchanged (and may or may not be alive depending on whether anything else refers to the object).

When you do a new assignment such as y = x, a new dictionary entry "y" is created that points to the same object as the entry for "x".

Objects like strings and integers are immutable. This simply means that there are no methods that can change the object after it has been created. For example, once the integer object one-thousand is created, it will never change. Math is done by creating new integer objects.

Objects like lists are mutable. This means that the contents of the object can be changed by anything pointing to the object. For example, x = []; y = x; x.append(10); print y will print [10]. The empty list was created. Both "x" and "y" point to the same list. The append method mutates (updates) the list object (like adding a record to a database) and the result is visible to both "x" and "y" (just as a database update would be visible to every connection to that database).

## When is "i += x" different from "i = i + x" in Python?

https://stackoverflow.com/a/15376520/17238613
