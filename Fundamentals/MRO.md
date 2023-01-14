## MRO
Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes. 
Especially it plays vital role in the context of multiple inheritance as single method may be found in multiple super classes.

### Case 1
This is a simple case where we have class C derived from both A and B. When method process() is called with object of class C then process() method in class A is called.
Python constructs the order in which it will look for a method in the hierarchy of classes. It uses this order, known as MRO, to determine which method it actually calls.
It is possible to see MRO of a class using mro() method of the class.

```python
class A:
    def process(self):
        print('A process()')
class B:
    pass
class C(A, B):
    pass

obj = C()  
obj.process()    
print(C.mro())   # print MRO for class C
```

The above diagram illustrates hierarchy of classes.
When run, the above program displays the following output:

A process()
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

From MRO of class C, we get to know that Python looks for a method first in class C. Then it goes to A and then to B. So, first it goes to super class given first in the list then second super class, from left to right order. Then finally Object class, which is a super class for all classes.

### Case 2

```python
class A:
    def process(self):
        print('A process()')

class B:
    def process(self):
        print('B process()')

class C(A, B):
    def process(self):
        print('C process()')

class D(C,B):
    pass
obj = D()
obj.process()

print(D.mro())
```

Running the above program will produce the following output:

Remember it goes from left to right. So it searches C first and all its super classes of C and then B and all its super classes. 
We can observe that in MRO of the output given below.

C process()
[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

### Case3: 

```python
class A:
    def process(self):
        print('A process()')
class B(A):
    pass


class C(A):
    def process(self):
        print('C process()')

class D(B,C):
    pass

obj = D()
obj.process()
```

Output of the above program is:

[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


So the original MRO will be:
D -> B -> A -> C -> A 

If you include object class also in MRO then it will be:
D -> B-> A -> object -> C -> A -> object 

👉 **But as A is super class of C, it cannot be before C in MRO. So, Python removes A from that position, which results in new MRO as follows:**
D -> B -> C -> A -> object 





