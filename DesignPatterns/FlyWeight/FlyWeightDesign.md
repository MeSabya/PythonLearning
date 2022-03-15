# Design patterns: Flyweight

*The flyweight software design pattern suggests creating an object that minimizes memory usage by sharing some of its data with other similar objects.*

Flyweight Design Pattern aims to minimize the number of objects required in the program during the runtime. A flyweight object has no visible difference from a normal object.

✓ Flyweight objects are immutable, once constructed, cannot be modified.

✓ In Python, we use Dictionary or List as a object pool, that stores reference to the object which has already been created.

👉 **Instantiating many heavy objects can be one of the very common reasons for the low system performance. This can be rectified by the flyweight pattern successfully.**

**Step1:** Flyweight pattern introduces a new object called ‘Flyweight’ to avoid the creation of a large number of heavy and high memory consumption objects.

**Step2:** 
Each “flyweight” object is divided into two pieces: the state-dependent (extrinsic) part, and the state-independent (intrinsic) part.

Extrinsic traits — Data(properties and funtionalities) that is unique to each individual object.
Intrinsic traits – Data that is common to several objects. 



