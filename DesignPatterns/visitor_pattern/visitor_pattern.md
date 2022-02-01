# The Visitor Design Pattern in Depth

👉 Visitor is a useful pattern when you have many objects of different types in your data structure and you want to apply some operation to several or all of them. 

👉 The pattern is helpful when you don’t know ahead of time all the operations you will need; 

👉 it gives you flexibility to add new operations without having to add them to each object type. 

👉 The basic idea is that a Visitor object is taken around the nodes of a data structure by some kind of iterator, and each node “accepts” the visitor, 
    allowing it access to that node object’s internal data.
    
>The Visitor pattern allows the application of the new operation without changing the class of any of the objects in the collection.
>Visitor Pattern suggests defining a separate interface (visitor) whose object implements the operation to be performed on elements of an object structure(i.e. hierarchy). For every additional operation, a new Visitor class is created.

## Components Of Visitor Pattern

**Visitor**: An abstract class used to declare the visit operations for all the types of visitable classes.

**ConcreteVisitor**: For each type of visitor all the visit methods, declared in abstract visitor, are implemented in ConcreteVisitor class.

**Visitable**: An abstract class that is used to declare accept operation. The Visitable class provides the access to the object(s) to be “visited” by the visitor class object.**

**ConcreteVisitable**: Classes that inherit the Visitable class and defines the accept operation. The visitor-object is passed to ConcereteVisitable- object(s) using the accept operation.

**ObjectStructure**: Class that contains all the objects that can be visited. ObjectStructure class also has a mechanism to iterate through all the objects in the object hierarchy.

### Example
Consider, we are working on an e-commerce website, where we can add different types of items in a shopping cart, now want to add a checkout button that will calculate the total amount.

```python
# Abstract visitable class — Item, having declaration of accept method.
class Item():
    """Visitable class"""
    @abstractmethod
    def accept(self):
        pass

class Shirt(Item):
    def __init__(self, price, size):
        self.price = price
        self.size = size

    def get_price(self):
        return self.price

    def get_size(self):
        return self.size

    def accept(self, visitor):
        return visitor.visit(self)
        
class Book(Item):
    def __init__(self, cost, genre):
        self.price = cost
        self.genre = genre

    def get_price(self):
        return self.price

    def get_genre(self):
        return self.genre

    def accept(self, visitor):
        return visitor.visit(self)   
        
# The abstract Visitor class        
class Visitor():
    """Abstract Vistor Class"""
    @abstractmethod
    def visit(self, item):
        pass
 
 # CartVisitor() class, serving as ConcereteVisitor and ObjectStructure class. 
 # And, having implementation of Visit() method, method that facilitates traversal the entire class hierarchy.
 
 class CartVisitor(Visitor):
    def visit(self, item):
        if isinstance(item, Book):
            cost = item.get_price()
            print("Book Genre: {}, cost = ${}".format(item.get_genre(), cost))
            return cost
        elif isinstance(item, Shirt):
            cost = item.get_price()
            print("Shirt, size{} cost = ${}".format(item.get_size(), cost))
            return cost
            
 def calculate_price(items):
    visitor = CartVisitor()
    sum = 0
    for item in items:
        sum = sum + item.accept(visitor)

    return sum
    
if __name__ == '__main__':
    items = [
        Shirt(10, "XL"),
        Shirt(15, "XXL"),
        Book(20, "Fiction"),
        Book(100, "Self Help"),        
    ]

    total = calculate_price(items)
    print("Total Cost = ${}".format(total))
    
```    
