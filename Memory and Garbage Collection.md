# Memory and Garbage Collection in Python

Firstly, let’s define two Python lists. They can be exactly the same in terms of the content.

a = [1, 2, 3]
b = [1, 2, 3]

![image](https://user-images.githubusercontent.com/33947539/153866590-7f4bb9a5-d750-4d65-83d6-3c0194b6f6da.png)

👉 ***Apparently, variables a and b are the same. However, does that mean these two variables are pointing to the same memory address? No. Let’s verify it.***

![image](https://user-images.githubusercontent.com/33947539/153866699-a7690807-336f-4da6-86f3-b467b9cd5679.png)

*The id() function will give us the “identity” of an object, which is indicated by an integer. As shown, the integers are different. So, variables a and b are pointing to different memory addresses although they are the same at the moment.*

If we create another variable a1 and let a1 = a, there is no new object created. Instead, a1 will point to the same memory address as of a.

![image](https://user-images.githubusercontent.com/33947539/153866796-119c21ed-77b9-4f4d-92a5-377cca73c589.png)

That makes sense, that’s why when we change a, a1 will also be updated.


Python follows two kinds of strategies:
      
      Garbage Collection
      Reference counting
      

👉 When ever a new object is created in python , python memory manager ensures that there is enough memory in the heap to allocate space to that object.

👉 In python , all objects are derived from PyObject a struct which has two properties reference count and pointer to the object.


```python
x == 100 // this will create a new object in heap
y == 100 // this will not create a new object as an object with           value 100 is already available on heap
print(id(x) == id(y)) // this returns true because x and y are pointing to same object on heap
x = 101  // now when new value is assigned  "101" is not available on heap , 
so new object is created and x points to this new object . 
In this case value at that location is not overwritten unlike other programming languages.
```

**Example**:

```python
import sys;

print("Initial reference count of 'dheeraj' : ",sys.getrefcount("dheeraj"))
x = "dheeraj"
print("After assigning to x , references to 'dheeraj' is incremented by 1: ",sys.getrefcount("dheeraj"))
print("Address of x",id(x))
y = "dheeraj"
print("After assigning to y , references to 'dheeraj' is incremented by 1 : ",sys.getrefcount("dheeraj"))
print("Address of y", id(y))

print("Does both x and y point to same object : ",id(x) == id(y))

x = 101
print("Address of x after re-assigning : ",id(x))
print("Address of y remains same :" ,id(y)) 
print("Does both x and y point to same object : ",id(x) == id(y))
print("Final reference count of :" , sys.getrefcount("dheeraj"))

print("Current Reference count of '101' is : ", sys.getrefcount(101) , " , Address : " ,id(101))

y = 101

print("Since this object is already available on heap , this points to same object : " , id(y) == id(101) , " \n Reference count : " ,sys.getrefcount(101))
```

![image](https://user-images.githubusercontent.com/33947539/173764579-e2ef8b33-bbba-4207-bef8-58ab70d97043.png)

#### What will increase the reference count?

1. The object is created and assigned to a variable.
2. The object is assigned to one more variable.
3. The object is passed in a function as an argument.
4. An object is appended into a container type.

👉 **Tricky One**:

```Lua
a = [1, 2, 3]
print(getrefcount(a))
```

👆 What should be the reference_count ?  Ans is : 2

***why it is 2?***
![image](https://user-images.githubusercontent.com/33947539/153867435-473985e0-35e8-4e95-b62d-6554890d008b.png)

**Answer is:**

In fact, when we use the getrefcount() function to query the reference count of an object, the function has to establish the reference to the object. That’s why the reference count is 2. It indicates that both the variable a and the function getrefcount() are referencing the list [1, 2, 3].




## Garbage Collection in Python

The job of the garbage collector is to track of the objects which can de-allocated.

Python uses below 2 algorithms for garbage collection:
      
      Reference counting
      Generational garbage collection
      
### Reference Counting
*Reference counting is a simple technique in which , whenever the reference count of an object reaches to “0” , then it is eligible for garbage collection and the memory allocated for that object is automatically de-allocated.*

```python
import sys

print("Initial reference count of 'python' : " ,sys.getrefcount("python") )

text = "python"
print("Current reference count" , sys.getrefcount("python"))

text2 = "python"
print("Current reference count after adding one more reference" , sys.getrefcount("python"))

print(id("python") , id(text))


lst = [text]
print("Current reference count after adding one more reference by adding that object to list" , sys.getrefcount("python"))


lst = [text,text2]
print("Current reference count after adding one more reference by adding that object to list" , sys.getrefcount("python"))

print("Reference count before passing object as input to the function : ",sys.getrefcount("python"))


def temp(inp):

  print("Reference count in function :" , sys.getrefcount("python"))

temp(text)


print("Reference count after function execution : " , sys.getrefcount("python"))
```

**output of the above**

```shell
Initial reference count of 'python' :  4
Current reference count 5
Current reference count after adding one more reference 6
139892114426800 139892114426800
Current reference count after adding one more reference by adding that object to list 7
Current reference count after adding one more reference by adding that object to list 8
Reference count before passing object as input to the function :  8
Reference count in function : 10
Reference count after function execution :  8
```

👉 ***By default python uses reference counting technique for garbage collection , which cannot be disabled (developer has no control over it).***

#### Disadvantages of Reference counting
But the issue with this technique is it has some overhead because , every object has to keep track of reference count for memory de-allocation and also memory de-allocation happens whenever an objects reference count becomes “0”.

Reference counting will not be able to detect the **cyclic references** and those objects will not be eligible for garbage collection.

Because of above problems , python also uses another technique called Generational Garbage Collection.

#### What is a cyclical reference or reference cycle?
It is a situation in which an object refers to itself. The simplest cyclical reference is appending a list to itself.
Reference counting alone can not destroy objects with cyclic references. If the reference count is not zero, the object cannot be deleted.

The solution to this problem is the second garbage collection method.

### Generational Garbage Collection

*This says that if an object survives for a set period of time, it’s expected to survive for longer. New objects tend to turn into garbage quicker than old objects.*

Using this hypothesis, this GC monitors the young objects more frequently, since they tend to die quickly and free up more space for the computer. As for the old objects, they can be monitored less frequently. This approach speeds up performance and reduces the pause time for the application.

![image](https://user-images.githubusercontent.com/33947539/153865547-c9371c20-1fba-4947-9658-71b8f3d01f8b.png)

👉 In generational garbage collectors, such as the one used in Java, objects are split into groups according to their age into multiple regions called generations, as shown in the diagram above. There is a Young Generation, Old Generation and Permanent Generation.

When a new object is created , that object is categorized into “generation 0” or "Young Generation".

Garbage collection is triggered automatically when a generation reaches its threshold and whatever objects remain in that generation after garbage collection are promoted to older generation.
If there are 2 generations reached threshold , always garbage collection choses older generation and then younger generation.


Python keeps track of every object in memory. 3 lists are created when a program is run. Generation 0, 1, and 2 lists.

Newly created objects are put in the Generation 0 list. A list is created for objects to discard. Reference cycles are detected. If an object has no outside references it is discarded. The objects who survived after this process are put in the Generation 1 list. The same steps are applied to the Generation 1 list. Survivals from the Generation 1 list are put in the Generation 2 list. The objects in the Generation 2 list stay there until the end of the program execution.



