

## why we need class method in python?
Class methods are typically useful when we need to access the class itself — for example, when we want to create a factory method, that is a method that creates instances of the class. In other words, classmethods can serve as alternative constructors.

```python

class Employee:
    NO_OF_EMPLOYEES = 0
  
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.increment_employees()
    def give_raise(self, amount):
        self.salary += amount
    @classmethod
    def employee_from_full_name(cls, full_name, salary):
        split_name = full_name.split(' ')
        first_name = split_name[0]
        last_name = split_name[1]
        return cls(first_name, last_name, salary)
    @classmethod
    def increment_employees(cls):
        cls.NO_OF_EMPLOYEES += 1
    @staticmethod
    def get_employee_legal_obligations_txt():
        legal_obligations = """
        1. An employee must complete 8 hours per working day
        2. ...
        """
        return legal_obligations
```

## What does the "yield" keyword do in Python?

**The yield keyword is reduced to two simple facts:**

- If the compiler detects the yield keyword anywhere inside a function, that function no longer returns via the return statement. Instead, it immediately returns a 
  lazy "pending list" object called a generator

- A generator is iterable. What is an iterable? It's anything like a list or set or range or dict-view, with a built-in protocol for visiting each element in a certain   order.

- Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly:

Original version:

```python
def some_function():
    for i in xrange(4):
        yield i

for i in some_function():
    print i
```

👉 This is basically what the Python interpreter does with the above code:

```python
class it:
    def __init__(self):
        # Start at -1 so that we get 0 when we add 1 below.
        self.count = -1

    # The __iter__ method will be called once by the 'for' loop.
    # The rest of the magic happens on the object returned by this method.
    # In this case it is the object itself.
    def __iter__(self):
        return self

    # The next method will be called repeatedly by the 'for' loop
    # until it raises StopIteration.
    def next(self):
        self.count += 1
        if self.count < 4:
            return self.count
        else:
            # A StopIteration exception is raised
            # to signal that the iterator is done.
            # This is caught implicitly by the 'for' loop.
            raise StopIteration

def some_func():
    return it()

for i in some_func():
    print i

```
For more insight as to what's happening behind the scenes, the for loop can be rewritten to this:

```python
iterator = some_func()
try:
    while 1:
        print iterator.next()
except StopIteration:
    pass

```

## References:
https://github.com/learning-zone/python-interview-questions

## How varibales are passed in Python, Is it pass by value or pass by reference ?

Python's variable passing style as call-by-object:

Objects are allocated on the heap and pointers to them can be passed around anywhere.

When you make an assignment such as x = 1000, a dictionary entry is created that maps the string "x" in the current namespace to a pointer to the integer object containing one thousand.

When you update "x" with x = 2000, a new integer object is created and the dictionary is updated to point at the new object. The old one thousand object is unchanged (and may or may not be alive depending on whether anything else refers to the object).

When you do a new assignment such as y = x, a new dictionary entry "y" is created that points to the same object as the entry for "x".

Objects like strings and integers are immutable. This simply means that there are no methods that can change the object after it has been created. For example, once the integer object one-thousand is created, it will never change. Math is done by creating new integer objects.

Objects like lists are mutable. This means that the contents of the object can be changed by anything pointing to the object. For example, x = []; y = x; x.append(10); print y will print [10]. The empty list was created. Both "x" and "y" point to the same list. The append method mutates (updates) the list object (like adding a record to a database) and the result is visible to both "x" and "y" (just as a database update would be visible to every connection to that database).

## When is "i += x" different from "i = i + x" in Python?

https://stackoverflow.com/a/15376520/17238613
