A normal reference increments the reference count on the object and prevents it from being garbage collected. 

This is not always desirable, 
- either when a circular reference might be present or 
- when building a cache of objects that should be deleted when memory is needed.

The weakref module supports weak references to objects. 


👉 Weak references allow you to reference an object without increasing its reference count. 
This means that if all strong references to the object are deleted, the object can be collected by Python's garbage collector,
even if weak references still exist.

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
import sys
import gc

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

print("Reference count for a:", sys.getrefcount(a))
print("Reference count for b:", sys.getrefcount(b))

# Setting up strong circular references
a.b = b
b.a = a

print("Reference count for a after circular reference:", sys.getrefcount(a))
print("Reference count for b after circular reference:", sys.getrefcount(b))

#setting up weak circular reference
#a.b = weakref.ref(b)
#b.a = weakref.ref(a)


#deleting objects
del a
del b

#gc.collect()

# Check if the objects have been collected
print("Objects collected, if any:")
for obj in gc.get_objects():
    if isinstance(obj, A) or isinstance(obj, B):
        print(f"Uncollected object: {obj}")

print("End of script")
```
Output of the code is:

```shell
Object A Created
Object B Created
Reference count for a: 2
Reference count for b: 2
Reference count for a after circular reference: 3
Reference count for b after circular reference: 3
Objects collected, if any:
Uncollected object: <__main__.A object at 0x75c4f71b3fd0>
Uncollected object: <__main__.B object at 0x75c4f71b3fa0>
End of script
Object A Destroyed
Object B Destroyed
```

### Now with weak reference

Comment this section of code in the above code:  

Setting up strong circular references
a.b = b
b.a = a

and uncommenting this section of code:

#setting up weak circular reference
#a.b = weakref.ref(b)
#b.a = weakref.ref(a)

```shell
Object A Created
Object B Created
Reference count for a: 2
Reference count for b: 2
Reference count for a after circular reference: 2
Reference count for b after circular reference: 2
Object A Destroyed
Object B Destroyed
Objects collected, if any:
End of script
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
## In reallife usecase why in the observer pattern it is necessary to use weak reference ..at the end we need an observer to notify to?

### Why Use Weak References in the Observer Pattern?

#### Automatic Resource Management:

If the subject holds strong references to its observers, those observers will remain alive as long as the subject exists, even if they are no longer needed elsewhere in the application.
This can lead to memory leaks, especially if observers are no longer in active use but are not explicitly removed from the subject's observer list.

```python
import weakref

class DataModel:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(weakref.ref(observer))

    def notify_observers(self):
        for ref in self._observers:
            observer = ref()
            if observer is not None:
                observer.update()
            else:
                # Optionally remove the observer if it's been collected
                self._observers.remove(ref)

class Window:
    def update(self):
        print("Window updated with new data.")

# Example usage
model = DataModel()

window1 = Window()
model.add_observer(window1)

window2 = Window()
model.add_observer(window2)

model.notify_observers()  # Both windows get notified

# Simulate closing window1
del window1

model.notify_observers()  # Only window2 gets notified; window1 is no longer alive
```

### Why Not Always Use Strong References?
If the subject kept strong references to window1 and window2:

**Even after window1 is "closed" (i.e., the window1 variable is deleted), the window object would remain in memory because the subject still holds a strong reference.This would cause a memory leak, as the window object (and any resources it holds) cannot be garbage collected.**

👉 By using weak references:

When window1 is deleted (or goes out of scope), the weak reference in the subject no longer prevents window1 from being garbage collected.
The next time the subject tries to notify its observers, it can skip over any observers that have been collected.

#### Handling None References

In scenarios where weak references are used:

The subject should check if the weak reference returns None before attempting to call the observer's update method.
If it returns None, this indicates that the observer has been garbage collected, and the subject can either ignore it or clean up its observer list by removing the None references.
