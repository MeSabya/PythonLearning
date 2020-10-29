'''
Does Python supports method overloading ?
Answer is No, How can you achieve it ??
By using Decorator pattern
For more info please follow :
https://medium.com/practo-engineering/function-overloading-in-python-94a8b10d1e08
'''

'''
step1:  
Learn to implement a decorator with arguments.
'''
registry = {}

class MultiMethod:
    def __init__(self, name):
        self.fun_name = name
        self.type_map = {}
        print("__int__ called")

    def register(self, types, name):
        print("MultiMethod Register called ", types, name)
        self.type_map[types] = name

    '''
    Here args are the arguments of the decorated function, here based on the argument types 
    Need to determine which function should be called 
    '''
    def __call__(self, *args):
        print("MultiMethod called ", *args)
        types = tuple(arg.__class__ for arg in args)
        fun = self.type_map[types]
        if fun is None:
            raise TypeError("No match Found")
        return fun(*args)

def overload(*types):
    def register(function):
        print("Register decorator called")
        fun_name = function.__name__
        print("Function name ", fun_name)
        mm = registry.get(fun_name)
        if mm is None:
            mm = registry[fun_name] = MultiMethod(fun_name)
        mm.register(types, function)
        return mm
    return register

@overload(int, int)
def area(len, breath):
    calc = len * breath
    return calc

@overload(int)
def area(radius):
    return 3.14 * radius*radius

@overload(str, str)
def add(first_name, last_name):
    return first_name + last_name

@overload(str, str, int)
def add(addr, country, pincode):
    return addr + country + pincode

print(add("sabya", "sachi"))
#print(area(3))
#print(area(5, 9))
