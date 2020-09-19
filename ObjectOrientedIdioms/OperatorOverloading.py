'''
Python permits operator overloading but within certain constraints:

Overloading the operators for built-in types is not allowed.
Creating new operators is not allowed.
Few operators can’t be overloaded, e.g., is, and, or and not.
'''

'''
How to add two vectors in python
'''
import itertools

class Vector(object):
    def __init__(self, vector):
        self.vector = vector
    def print(self):
        print(list(self.vector))
    def __add__(self, other):
        return Vector(i+j for i, j in itertools.zip_longest(self.vector, other.vector))

v1 = Vector([2, 4, -1])
v2 = Vector([3, 2, 5])

v3 = v1 + v2
v3.print()