## How does Python's memory model work for immutable types like strings and integers?
Great question — understanding how Python handles immutable types like strings and integers is key to writing efficient and bug-free code.

### 🔒 What is an immutable type?
An immutable object cannot be changed after it's created.

Examples:
int, float, str, tuple, frozenset

### 1. Object Identity and Interning
Python often reuses immutable objects to save memory and improve performance. This is done via interning.

#### 🔢 Small Integer Caching (Integer Interning)
Python pre-allocates small integers in the range [-5, 256] during startup. These are reused everywhere in the program.

```python
a = 100
b = 100
print(a is b)  # ✅ True — same object (interned)

a = 300
b = 300
print(a is b)  # ❌ False — not interned
```

Why [-5, 256]? These are commonly used values, so caching them saves memory and boosts performance.

#### 🧵 String Interning
Python automatically interns some strings:

Short strings

Strings that look like identifiers (e.g., 'foo', 'x123')

Compile-time constants

```python
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # ✅ Often True (interned)

s3 = "hello world"
s4 = "hello world"
print(s3 is s4)  # ❌ Often False (not auto-interned)
```

To explicitly intern a string:

```python
import sys
s1 = sys.intern("hello world")
s2 = sys.intern("hello world")
print(s1 is s2)  # ✅ True
```

#### 2. Reassignment Creates New Objects
Immutable means no in-place mutation. Any operation that modifies the value creates a new object.

```python
x = 10
print(id(x))   # e.g., 140394400855184

x += 1
print(id(x))   # Different ID — new object!

s = "hello"
print(id(s))

s += " world"
print(id(s))  # New object created
```

## What is the difference between is and ==? Where might using is cause a bug? 

### ✅ == (Equality)
Compares values of two objects.

- Returns True if the contents are the same.
- Calls the __eq__() method under the hood.

### ✅ is (Identity)
- Compares object identity
- Returns True only if both variables point to the exact same object in memory (i.e., same id()).

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True — same contents
print(a is b)  # False — different objects in memory

c = a
print(a is c)  # True — both refer to the same object
```

### When is might cause bugs

#### 1. With small integers or strings (due to interning):
Python caches small integers [-5, 256] and some short strings for performance, so they might seem like the same object:

```python
x = 256
y = 256
print(x is y)  # True

x = 257
y = 257
print(x is y)  # False — this may surprise you!
```

```python
a = "hello"
b = "hello"
print(a is b)  # True — often, due to interning

a = "".join(["he", "llo"])
print(a == b)  # True
print(a is b)  # False — different objects
```

👉 So using is to compare strings or numbers can lead to subtle bugs.

## Find the output
<details>

```python
def f(x, lst=[]):
    lst.append(x)
    return lst

print(f(1))
print(f(2))
print(f(3, []))
print(f(4))
```

- A) [1] [2] [3] [4]
- B) [1] [1, 2] [3] [1, 2, 4]
- C) [1] [1, 2] [3] [1, 2, 4]
- D) [1] [2] [3] [4]

### ✅ Answer: B
Explanation: Mutable default arguments persist across calls.
</details>

## Find the Output
<details>

```python
class A:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val
a = A(10)
b = A(10)
print(a == b, a is b)
```

A) True True
B) True False
C) False False
D) Error

#### ✅ Answer: B
Explanation: == calls __eq__, but a is b compares object identity.
</details>

## functools.lru_cache Tricky questions
<details>
    
### What will this print?
```python
import functools

@functools.lru_cache(maxsize=2)
def square(n):
    print(f"Computing square({n})")
    return n * n

print(square(2))
print(square(3))
print(square(2))
print(square(4))
print(square(3))
```
#### Output
```shell
Computing square(2)  
4  
Computing square(3)  
9  
4  
Computing square(4)  
16  
Computing square(3)  
9  
```
#### Explanation
- maxsize=2 means only the last two results are cached.
- When square(4) is computed, square(2) gets evicted.
- Calling square(3) again retrieves it from cache, while square(2) would have needed recomputation.

### What will happen if you run this?
```python
import functools

@functools.lru_cache(maxsize=3)
def add(a, b):
    return a + b

print(add(2, 3))
print(add(2.0, 3.0))
```
#### Output
5 and 5

By default, lru_cache() does not distinguish types.

add(2,3) and add(2.0,3.0) are treated as the same cache entry.

### What happens if we modify a mutable argument?
```python
import functools

@functools.lru_cache(maxsize=3)
def process(data):
    data.append(10)
    return sum(data)

print(process([1, 2, 3]))
print(process([1, 2, 3]))
```
#### Explanation
- Lists are mutable, and lru_cache() only works with hashable arguments.
- This raises a TypeError because lists are unhashable.

### How can we fix the previous issue?
```python
import functools

@functools.lru_cache(maxsize=3)
def process(data):
    return sum(data) + 10

print(process(tuple([1, 2, 3])))
print(process(tuple([1, 2, 3])))
```
- 16 (cached) and 16
- Tuples are immutable, so they can be cached.

### What will this print?
```python
import functools

@functools.lru_cache(maxsize=3, typed=True)
def add(a, b):
    return a + b

print(add(2, 3))
print(add(2.0, 3.0))
```
The typed=True flag ensures that int and float versions are treated separately.

add(2,3) and add(2.0,3.0) are stored as separate cache entries.

### What happens here?
```python
import functools

@functools.lru_cache(maxsize=3)
def counter():
    counter.count += 1
    return counter.count

counter.count = 0
print(counter())
print(counter())
```
#### Explanation
1 and 1

lru_cache() only allows caching functions with arguments.

Since counter() has no arguments, it always returns the cached result (1).

### What happens if maxsize=0?

```python
import functools

@functools.lru_cache(maxsize=0)
def power(n):
    return n ** 2

print(power(3))
print(power(3))
```
A) 9 and 9
Explanation:

maxsize=0 disables caching, meaning power(3) is always recomputed.
</details>


## What is the var() function in Python?

The var() function is part of the standard library in Python and is used to get an object’s _dict_ attribute. 
The returned _dict_ attribute contains the changeable attributes of the object. 
This means that when we update the attribute list of an object, the var() function will return the updated dictionary.

The var() function returns a changeable _dict_ attribute of the passed object. This object can be a module, class instance, class, etc. When no parameter is passed, var() returns the local symbol table of the object passed as a dictionary.

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
The difference between type() and isinstance() in Python lies in their usage and behavior when checking the type of an object.

### type()
- Purpose: Returns the exact type of an object.
- Usage: type(object) returns the type of object.

Example:
```python
a = 10
print(type(a))  # Output: <class 'int'>
```

Limitations: type() is strict and does not consider inheritance. It checks if the object's type is exactly the type provided.

### isinstance()
Purpose: Checks if an object is an instance of a class or a subclass thereof.

Usage: isinstance(object, classinfo) returns True if object is an instance of classinfo or any subclass thereof, and False otherwise.

Example:

```python
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(isinstance(d, Dog))     # Output: True
print(isinstance(d, Animal))  # Output: True
```
Advantages: isinstance() is more flexible than type() because it supports inheritance. It is generally preferred when checking an object's type in a polymorphic setting.

Key Differences
Strictness: type() is strict and does not recognize subclasses, whereas isinstance() checks for both the exact class and subclasses.

### Common Use Cases:
- Use type() when you need to know the exact type of an object.
- Use isinstance() when you want to check if an object is of a specific type or a derived type (inherited class).

### Example Comparing Both
```python
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(type(d) == Dog)       # Output: True
print(type(d) == Animal)    # Output: False

print(isinstance(d, Dog))   # Output: True
print(isinstance(d, Animal)) # Output: True
```
In this example, type(d) == Animal is False because d is of type Dog, not Animal. However, isinstance(d, Animal) is True because Dog is a subclass of Animal.

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

## Output1

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()  # What will be printed?
```
### Explanation:

D inherits from both B and C. When a method is called on an object of class D and that method is not defined in D, Python looks for the method in the base classes in a specific order known as the Method Resolution Order (MRO).

The MRO is determined by the order of base classes specified in the class definition. In this case, the MRO for class D is [D, B, C, A].

The show method is called on obj, which is an instance of class D. Python looks for the show method in class D, then in class B, then in class C, and finally in class A.

**The show method is found in class B. Therefore, the show method from class B is executed, and the output will be: B**

## Output2

```python
values = [1, 2, 3, 4, 5]
squares_lc = [x**2 for x in values]
squares_ge = (x**2 for x in values)

print(squares_lc)  # What will be printed?
print(squares_ge)  # And here?
```
### Explanation
Output: 
[1, 4, 9, 16, 25]
<generator object <genexpr> at ...

## Output3
```python
User
x = 10
def func():
    x += 1
    print(x)

func()
```







