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

### What Problem arises due to Circular Reference?

The problem occurs when the classes of any objects involved in the circular reference have a custom ```__del__``` function.

Consider the following Python code for instance:

````
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

