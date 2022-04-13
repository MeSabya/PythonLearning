# Builder pattern

👉 The builder pattern is a type of creational design pattern, designed to provide a flexible solution to various object creation problems in object-oriented programming.

👉 The Builder design pattern intends to separate the construction of a complex object from its actual representation so that we can use the same construction process to create different representations for the same object.

**Simply said, Builder design patterns represent a method to builds a complex object using simple objects and a step-by-step approach.**

### The Builder design pattern solves problems like:
- How can a class create different representations of a complex object?
- How can a class that includes creating a complex object be simplified?

## Example 

The manufacturer can produce different models depending upon the features he chooses to provide in a car. Let’s define methods to add or subtract the features.

```python
class Car():
    '''The Product'''
    def __init__(self):
        self.autonomous_driving = False
        self.sunroof = False
        self.fuel = None
     
    #Methods to add features
    def addAutonomous_driving(self):
        self.autonomous_driving = True
    def addSunroof(self):
        self.sunroof = True
    def addFuel(self, fuel="Electric"):
        self.fuel = fuel
 
    #Returning information about car
    def __str__(self):
        return f'Autonomous driving: {self.autonomous_driving} | Sunroof: {self.sunroof} | Fuel: {self.fuel}'
 
 ```
 
 The class Car has all the features and methods to add them. Now for each instance, all the features would be added via explicit method calls (addAutonomous_driving, addSunroof), depending upon the car model to produce.
 
 ```python
 #First instance name ModelOneModelOne = Car()
ModelOne.addAutonomous_driving()
ModelOne.addSunroof()
ModelOne.addFuel("Petrol")
print("Details of car:", ModelOne)
 
#Second instance named ModelTwo
ModelTwo = Car()
ModelTwo.addAutonomous_driving()
ModelTwo.addFuel()
print("Details of car:", ModelTwo)

#Third instance named ModelThree
ModelThree = Car()
ModelThree.addAutonomous_driving()
ModelThree.addSunroof()
ModelThree.addFuel("Diesel")
print("Details of car:", ModelThree)

```

Observe the complexity in the creation of each instance(object) via explicit method calls, if the number of instances increases the code will become more complex and chaotic. This is where the builder pattern helps us.

The Builder Pattern resolves this issue and brings order to this chaos by removing the complexity involved. 
This is achieved by segregating the entire process into four roles. Consider creating different models of car with the Builder design pattern’s four roles-

1. **The Product**: Complex object to be made. (e.g Car)
2. **Abstract Builder Interface**: Provides necessary interfaces required to build the object. It is abstract because it is not instantiated, it is only inherited by the Builder.
3. **Builder**: Inherits the Abstract Builder and implements the above interfaces of the Abstract Builder class; provides methods to create components of the product.
4. **Director**: In charge of creating the product, assembling various components and then delivering it. It uses the concrete builder object. 

```python
class Car:
    '''The Product'''
    def __init__(self):
        self.autonomous_driving = None
        self.sunroof = None
        self.fuel = None

    #Returning information of the car 
    def __str__(self):
        return f'Autonomous_driving: {self.autonomous_driving} | Sunroof: {self.sunroof} | Fuel: {self.fuel}'
        
class AbstractBuilder:
  '''Abstract Builder Interface'''
  def __init__(self):
      self.car = None
  def createNewCar(self):
      self.car = Car()       

class ConcreteBuilder(AbstractBuilder):
    '''Actual Builder'''
    def addAutonomous_driving(self, AD):
        self.car.autonomous_driving = AD
    def addSunroof(self, SR):
        self.car.sunroof = SR
    def addFuel(self, fuel):
        self.car.fuel = fuel

class Director:
    '''Director'''
    def __init__(self, builder):
        self._builder = builder
    def constructCar(self, AD=False, SR=False, fuel="Electric"):
        self._builder.createNewCar()
        self._builder.addAutonomous_driving(AD)
        self._builder.addSunroof(SR)
        self._builder.addFuel(fuel)
        return self._builder.car

#Instantiation of Builder
concreteBuilder = ConcreteBuilder()
#Calling Director
director = Director(concreteBuilder)
#Getting Our Product
ModelOne = director.constructCar()
print("Details of car:", ModelOne)

ModelTwo = director.constructCar(True, True, "Diesel")
print("Details of car:", ModelTwo)

ModelThree = director.constructCar(True, False, "Petrol")
print("Details of car:", ModelThree)

```
👉 *Construction of complex objects need not have only one Builder, rather there can be several Builders depending upon the complexity of the builder itself.*


## Consider using this when:

1. Object contains a lot of attributes
2. Builder pattern may be very useful while writing Unit Tests. When in order to construct the object under the test, need to pass a lot of parameters to the constructor and some of these parameters are completely irrelevant for the specific test. Builder class creation with separate methods for each parameter that should be tested, which returns by the end complete object under the test will help to write many UTs effectively, without duplicating the code.

3. Building an XML document with HTML elements ```(<html>,<h1>,<h2>, <body>,<p> and etc)```
4. Building a smartphone object with attributes like RAM, size, resolution, OS, waterproof and so on.


## Reference:
https://github.com/rommel-sunga/design-patterns-for-humans-python#-builder
https://medium.com/@analempert/10-design-patterns-with-day-to-day-examples-e4f256d8439





 
 
 
