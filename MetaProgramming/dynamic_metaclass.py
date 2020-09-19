'''
The potential of a code to be able to manipulate itself is called meta-programming.
As far as meta-programming via functions is concerned, we had already covered it when we discussed decorators.
Python also supports meta-programming for classes by introducing meta-classes.

What is a metaclass?
Just like we create objects of different classes,
a class is also an object of something we can call as metaclass.
A special class "type" creates a Class object.

An ordinary class defines the behavior of its object, whereas a metaclass defines the behavior of an ordinary class and its instance.
A metaclass can add or subtract a method or field to a regular class.

# Class definition
class A: pass

# Modifying class after its definition

A.x = 10  # Adding a field

A.function = lambda self: print('Number is: ', A.x) # Adding a method


obj = A()
obj.function()
'''

#########################################
#             Example1:
# How can you create a dynamic class, like below:
# class A:
#   pass
#
# class B(A):
#   x = 0
######################################
A = type('A', (), {})
B = type('B', (A,), dict(x=0))

obj = B()
print(obj.x)
print(obj.__class__)
print(obj.__class__.__bases__)

'''
In the above case, <bases> (middle parameter in type() call)is a tuple with a single element A showing that B inherits from A. 
And, one attribute x is placed in the namespace of the class B.
'''
######################################
#          Example2
##########################################
'''
How can you create a dynamic class, like below:
class Foo:
  n = 1
 
  def function(self):
    return self.n * 2
'''
Foo = type('Foo', (), {'n':1, 'function':lambda x:x.n*2})
foo = Foo()
print(foo.function())