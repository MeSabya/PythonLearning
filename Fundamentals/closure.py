'''
When (and why) should we use closures in python instead of classes?
->Closure has a special ability to access other variables local to the scope it was created in.
->In many cases, the only reason we might have a single-method class is to store additional state for the use in method.

Problem Alert: Is it good to use class to just store additional state like above example?.
No, definetly not. So then what’s the solution?
'''

'''
import requests
class SourceTemplate:
    def __init__(self, url):
        self.url = url
    def load(self, **kwargs):
        return requests.get(self.url.format_map(kwargs))
github = SourceTemplate('https://api.github.com/repositories?since={since}')
github.load(since=200).json()

# In above example, the only purpose of using SourceTemplate class
# is to hold the url value some palce so that it can be used in load method.

def sourcetemplete(url):
    def load(**kwargs):
        return requests.get(url.format_map(kwargs))
    return load
load = sourcetemplete('https://api.github.com/repositories?since={since}')
load(since=200).json()
'''

'''
A key feature of a closure is that it remembers the enviroment in which it was defined”. 
This is the reason how function remembers the value of the url argument, uses it in subsequent calls.
'''

'''
Why to should we use closure?
i. to replace hard coded constants.
ii. to reduce the use of global variables
iii. Since it wrok as callback function, it provides some sorts of data hiding
iv. provide an object oriented solution to the problem
'''

'''
Now one of the interesting concepts late binding in closures.
Python’s closures are late binding. 
This means that the values of variables used in closures are looked up at the time the inner function is called.
Saying that guess the output of the following: 
A list containing five functions that each have their own closed-over i variable that multiplies their argument, 
So expected output is :
0
2
4
6
8

But the actual output is 
8
8
8
8
8
'''

def create_multipliers1():
    return [lambda x : i * x for i in range(5)]
'''
The above can be written as:
'''
def create_multipliers2():
    multipliers = []
    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)
    return multipliers

for multiplier in create_multipliers2():
    print(multiplier(2))

'''
In the above, whenever any of the returned functions are called, the value of 
i is looked up in the surrounding scope at call time. 
By then, the loop has completed and i is left with its final value of 4.
'''

'''
#####################################
                What should instead ?
####################################################3
'''
def create_multipliers_sol():
    multipliers = []
    for i in range(5):
        def multiplier(x, i=i):
            return i * x
        multipliers.append(multiplier)
    return multipliers

print("create_multipliers_sol 1")
for multiplier in create_multipliers_sol():
    print(multiplier(2))

'''
What we are doing here is we are using pythons default arguments concept.
Python’s default arguments are evaluated once when the function is defined, not each time the function is called.
This means that if you use a mutable default argument and mutate it, 
you will and have mutated that object for all future calls to the function as well.

here by default we are assigning i value to i as default argument while declaring the function.
All the future calls to multiplier will use the same "i" value. 
'''

from functools import partial
from operator import mul

def create_multipliers_sol2():
    return [partial(mul, i) for i in range(5)]

print("create_multipliers_sol  2")
for multiplier in create_multipliers_sol2():
    print(multiplier(2))


