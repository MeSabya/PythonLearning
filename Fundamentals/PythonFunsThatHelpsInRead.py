#vars()
'''
The vars() function will return the __dict__,
which is a dictionary used to store an object’s attributes. Its result is the same as calling the __dict__ directly.
'''

class TopDeveloper:
    def __init__(self):
        self.name = "Yang"
        self.country = "UK"

me = TopDeveloper()
print(vars(me))
print(vars(me) is me.__dict__)

year = 2020
#print("vars on year", vars(year))
"""
It’s not necessarily that all objects have the __dict__, so we can only use the vars() method in parts of objects.
In the above example print("vars on year", vars(year)) will raise TypeError.
"""

'''
The dir() function helps us demonstrate a list of names in the corresponding scope.
'''
print(dir(me))