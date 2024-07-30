Descriptors are used when an object is assigned to a class attribute and then accessed through an instance.

Descriptor Methods

```shell
__get__(self, instance, owner): Part of the descriptor protocol, used to customize the behavior of getting an attribute.
__set__(self, instance, value): Part of the descriptor protocol, used to customize the behavior of setting an attribute.
__delete__(self, instance): Part of the descriptor protocol, used to customize the behavior of deleting an attribute.
```

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

__getattr__(self, name): Called when an attribute is not found in an object’s __dict__. This acts as a fallback method.

__getattribute__(self, name): Called every time an attribute is accessed on an instance, regardless of whether it exists or not. This allows for extensive customization of attribute access.
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

## 


