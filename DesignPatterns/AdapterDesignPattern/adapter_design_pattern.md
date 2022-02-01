# Adapter Design Pattern

👉 *The Adapter design pattern is a structural design pattern, which suggests having an interface acting as a bridge between two incompatible interfaces to collaborate. This pattern combines the functionalities of two independent interfaces.*

What is an Adapter?

- A real-life example could be the case of a card reader, which acts as an adapter between a memory card and a laptop.
- In techincal terms, Adapter: A construct that adapts an existing interface X to conform to the required interface Y.

**The design pattern got its name because its purpose is the same – adapting one input to a different predetermined output.**

👉 There are some terminologies, worth knowing when working with Adapter Design Patterns.

**Adaptee**: The existing class or interface.

**Adapter**: The class in charge to cater the client’s needs.

**Client**: The class who wishes to communicate with adaptee, but incompatible.

```python
from abc import abstractmethod

#The client - New interface
class Client:
    def __init__(self) -> None:
        self._adaptee = Adaptee()

    @abstractmethod
    def request(self):
        pass

#The existing interface
class Adaptee:  
    def specific_request(self):
        pass

#Adapter the interface of Adaptee to the Target(i.e. client) interface.
class Adapter(Client):    
    def request(self):
        self._adaptee.specific_request()

#The diver code
def main():
    adapter = Adapter()
    adapter.request()


if __name__ == "__main__":
    main()
    
 ```   
