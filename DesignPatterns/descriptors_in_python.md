```python
class Foo:
    def __init__(self):
        self.x = 10
    def __get__(self, name):
        print('__get__ called')

    def __getattr__(self,name):
        return name
    def __getattribute__(self, name):
        if name == 'bar':
            raise AttributeError
        return 'getattribute'

f = Foo()
print(f.x)
print(f.baz)
print(f.bar)
```

## __get__ Vs __getattr__ Vs __getattribute__ 

```shell
__get__: Used with descriptors to control access to a specific attribute.

 __getattr__: A fallback method that is only called when an attribute is not found through normal means.

__getattribute__: Intercepts every attribute access and allows for extensive customization but requires care to avoid infinite recursion.
```

## Can you explain why __get__ called is not printed in the above example?

The __get__ method you defined in the Foo class isn't being called because __get__ is part of the descriptor protocol, which means it is used when an instance of the class (which has __get__ method) is accessed as an attribute of another class.

To make __get__ be called, you need to have an instance of Foo as an attribute of another class. Here’s how you can do it:

```python
class Foo:
    def __init__(self):
        self.x = 10

    def __get__(self, instance, owner):
        print('__get__ called')
        return self

    def __getattr__(self, name):
        return name

    def __getattribute__(self, name):
        if name == 'bar':
            raise AttributeError
        return super().__getattribute__(name)  # use the parent class's __getattribute__ to avoid infinite recursion

class Container:
    foo = Foo()

c = Container()
print(c.foo)  # This will call Foo's __get__ method
```

