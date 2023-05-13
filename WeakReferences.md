A normal reference increments the reference count on the object and prevents it from being garbage collected. 

This is not always desirable, 
- either when a circular reference might be present or 
- when building a cache of objects that should be deleted when memory is needed.

The weakref module supports weak references to objects. 

## What is Circular Reference in Python? Problem it causes and how to handle it.
When two objects in Python holds reference of each other, it is termed as cyclic or circular reference.
This occurs when object A’s property refers to object B, and object B’s property refers back to object A.

### Example 1: Circular Reference between Objects of the different class

```python
class A:
    def display(self):
        print('A: self: {0}, b:{1}'.format(hex(id(self)), hex(id(self.b))))
        
class B:
    def display(self):
        print('B: self: {0}, a:{1}'.format(hex(id(self)), hex(id(self.a))))

#two objects of different classes
a = A()
b = B()

#referring to each other
a.b = b
b.a = a

#display the circular reference
a.display()
b.display()
```

### Example 2: Circular Reference between Objects of the same class

```python
class X(str):
    def display(self, second):
        print(f"{self}: self: {hex(id(self))}, {second}: {hex(id(second))}")

#two objects of the same class
a = X('A')
b = X('B')

#referring each other
b.a = a               
a.b = b

#display the circular reference
a.display(a.b)
b.display(b.a)
```

Notice, each of the two objects is storing the reference of the other as a property, thus forming a circular reference.

### Example3 

```python 
Circular References
In [8]: l1 = [1,] ; l2 = [2,]

In [9]: l1.append(l2); l2.append(l1)

In [10]: l1
Out[10]: [1, [2, [...]]]

In [11]: l2
Out[11]: [2, [1, [...]]]

In [12]: l1[1]
Out[12]: [2, [1, [...]]]

In [13]: l2[1][1][1]
Out[13]: [1, [2, [...]]]
```


### What Problem arises due to Circular Reference?

The problem occurs when the classes of any objects involved in the circular reference have a custom ```__del__``` function.

Consider the following Python code for instance:

```python
class A:
    def __init__(self):
        print("Object A Created")
        
    def __del__(self):
        print("Object A Destroyed")
        
class B:
    def __init__(self):
        print("Object B Created")
        
    def __del__(self):
        print("Object B Destroyed")

#creating two objects
a = A()
b = B()

#setting up circular reference
a.b = b
b.a = a

#deleting objects
del a
del b
```

```shell
Output:

Object A Created
Object B Created
```

Here, both objects a and b are holding reference of the other and has a custom ```__del__``` function.
In the end, when we try to delete the object manually, the ```__del__``` methods were not called, indicating that the objects were not destroyed, thus causing a memory leak.

In such a case, the garbage collector of Python gets confused as to what order it should call the ```__del__``` methods and therefore it is not able to collect the objects for the clearance of the memory,

**Although this problem is resolved as PEP 442 in Python 3.4, it still exists in Python versions < 3.4.**

### How to Handle Memory Leak in Circular Reference?

We can prevent memory leaks caused by circular references in two ways::

- Manually deleting each reference.
- Using weakref.

Manually deleting each reference is not a good option because we as programmers would have to think of the point where we should delete the references, whereas in the case of weakref we don’t have to.

```python
import weakref

class A:
    def __init__(self):
        print("Object A Created")
        
    def __del__(self):
        print("Object A Destroyed")
        
class B:
    def __init__(self):
        print("Object B Created")
        
    def __del__(self):
        print("Object B Destroyed")

#creating two objects
a = A()
b = B()

#setting up weak circular reference
a.b = weakref.ref(b)
b.a = weakref.ref(a)

#deleting objects
del a
del b
```

## How weakref can be used to delete the useless objects?
To illustrate the difference between memory handling with a regular dictionary and WeakValueDictionary, let’s go experiment with explicitly calling the garbage collector again:

```python
import gc
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_LEAK)

class ExpensiveObject(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'ExpensiveObject(%s)' % self.name
    def __del__(self):
        print '(Deleting %s)' % self
        
def demo(cache_factory):
    # hold objects so any weak references 
    # are not removed immediately
    all_refs = {}
    # the cache using the factory we're given
    print 'CACHE TYPE:', cache_factory
    cache = cache_factory()
    for name in [ 'one', 'two', 'three' ]:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o # decref

    print 'all_refs =',
    pprint(all_refs)
    print 'Before, cache contains:', cache.keys()
    for name, value in cache.items():
        print '  %s = %s' % (name, value)
        del value # decref
        
    # Remove all references to our objects except the cache
    print 'Cleanup:'
    del all_refs
    gc.collect()

    print 'After, cache contains:', cache.keys()
    for name, value in cache.items():
        print '  %s = %s' % (name, value)
    print 'demo returning'
    return

demo(dict)
print
demo(weakref.WeakValueDictionary)
```

👉 Output
```shell
$ python weakref_valuedict.py

CACHE TYPE: <type 'dict'>
all_refs ={'one': ExpensiveObject(one),
 'three': ExpensiveObject(three),
 'two': ExpensiveObject(two)}
Before, cache contains: ['three', 'two', 'one']
  three = ExpensiveObject(three)
  two = ExpensiveObject(two)
  one = ExpensiveObject(one)
Cleanup:
After, cache contains: ['three', 'two', 'one']
  three = ExpensiveObject(three)
  two = ExpensiveObject(two)
  one = ExpensiveObject(one)
demo returning
(Deleting ExpensiveObject(three))
(Deleting ExpensiveObject(two))
(Deleting ExpensiveObject(one))

CACHE TYPE: weakref.WeakValueDictionary
all_refs ={'one': ExpensiveObject(one),
 'three': ExpensiveObject(three),
 'two': ExpensiveObject(two)}
Before, cache contains: ['three', 'two', 'one']
  three = ExpensiveObject(three)
  two = ExpensiveObject(two)
  one = ExpensiveObject(one)
Cleanup:
(Deleting ExpensiveObject(three))
(Deleting ExpensiveObject(two))
(Deleting ExpensiveObject(one))
After, cache contains: []
demo returning
```
