***Facade Pattern provides a unified and simple interface over a complex set of classes in a system, thus making the system easier to use.***

## Real-life example:

**Example1:**

Consider a Grocery shop. Where items are organized with an inventory management system. But, the customer need not know about the inventory, so it’s preferable that the customer must ask the shopkeeper with the list of items, as the shopkeeper knows where each item is located. Here the shopkeeper is serving as the Facade interface.
Customers need the items but they don’t know about inventory(Complex sub-systems), so there is a shopkeeper (A simple interface) who searches the items on behalf of customers.

**Example2:**

This pattern can be seen in the Python standard library when we use the isdir function. Although a user simply uses this function to know
whether a path refers to a directory, the system makes a few operations and calls other modules (e.g., os.stat) to give the result.


**The word Facade referred to an outer lying interface of a complex system, consists of several sub-systems.**


In short, Facade Pattern suggests defining a facade interface that should mask the complexity of the underlying system and should access the system on behalf of a client, hiding the implementation detail.

![image](https://user-images.githubusercontent.com/33947539/169802813-84f9bb63-7644-4f3d-8264-74581b24c976.png)

![image](https://user-images.githubusercontent.com/33947539/169803170-51d251a6-e140-4358-9cb9-f656e75ef7b2.png)

```python
class CPU:
    """
    Simple CPU representation.
    """

    def freeze(self):
        print("Freezing processor.")

    def jump(self, position):
        print("Jumping to:", position)

    def execute(self):
        print("Executing.")


class Memory:
    """
    Simple memory representation.
    """

    def load(self, position, data):
        print(f"Loading from {position} data: '{data}'.")


class SolidStateDrive:
    """
    Simple solid state drive representation.
    """

    def read(self, lba, size):
        return f"Some data from sector {lba} with size {size}"


class ComputerFacade:
    """
    Represents a facade for various computer parts.
    """

    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


def main():
    """
    >>> computer_facade = ComputerFacade()
    >>> computer_facade.start()
    Freezing processor.
    Loading from 0x00 data: 'Some data from sector 100 with size 1024'.
    Jumping to: 0x00
    Executing.
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
    
```    
