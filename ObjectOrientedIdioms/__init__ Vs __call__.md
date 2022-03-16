# What is the difference between __init__ and __call__?

👉 *Instances of Classes (aka Objects), can be treated as if they were functions: pass them to other methods/functions and call them. In order to achieve this, the __call__ class function has to be specialized.*

def __call__(self, [args ...]) It takes as an input a variable number of arguments. Assuming x being an instance of the Class X, x.__call__(1, 2) is analogous to calling x(1,2) or the instance itself as a function.

In Python, __init__() is properly defined as Class Constructor (as well as __del__() is the Class Destructor). Therefore, there is a net distinction between __init__() and __call__(): the first builds an instance of Class up, the second makes such instance callable as a function would be without impacting the lifecycle of the object itself (i.e. __call__ does not impact the construction/destruction lifecycle) but it can modify its internal state (as shown below).

```python

class Stuff(object):

    def __init__(self, x, y, range):
        super(Stuff, self).__init__()
        self.x = x
        self.y = y
        self.range = range

    def __call__(self, x, y):
        self.x = x
        self.y = y
        print '__call__ with (%d,%d)' % (self.x, self.y)

    def __del__(self):
        del self.x
        del self.y
        del self.range

>>> s = Stuff(1, 2, 3)
>>> s.x
1
>>> s(7, 8)
__call__ with (7,8)
>>> s.x
7

```
