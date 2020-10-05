import copy

class Person(object):
    def __init__(self, parents, siblings):
        self.parents = parents
        self.siblings = siblings
    def __repr__(self):
        return ' '.join(self.parents) + " "+ ' '.join(self.siblings)

person1 = Person(["Raj", "simran"], ["chintu", "pintu"])
person2 = person1
print("person2 members are: ", person2, "person1 members are: ", person1)
print(person1 is person2) #True

person3 = copy.copy(person1)
print(person1 is person3) #o/p False
person3.siblings.append("Mantu")
print("person3 members are: ", person3, "person1 members are: ", person1)

person4 = copy.deepcopy(person1)
person4.siblings.append("Hunnn")
print("person4 members are: ", person4, "person1 members are: ", person1)

# Example1:
#######################################################
print("Example1")
l1 = [1, 2, 3]
l2 = list(l1)

l1[0] = 4
print("print l1", l1)
print("Print l2", l2)

# Example 2
##########################################################
print("Example2")
l3 = [[1, 2, 3], [4, 5, 6]]
l4 = list(l3)

l3[0][0] = 4
print("print l1", l1)
print("Print l2", l2)

#Example 3
###########################################################
print("Example3")
l5 = [[1, 'a'], [2, 'b'], [3, 'c']]
l6 = list(l5)

l5.append([4, 'd'])
print(l5)
print(l6)

'''
Output:

person2 members are:  Raj simran chintu pintu person1 members are:  Raj simran chintu pintu
True
False
person3 members are:  Raj simran chintu pintu Mantu person1 members are:  Raj simran chintu pintu Mantu
person4 members are:  Raj simran chintu pintu Mantu Hunnn person1 members are:  Raj simran chintu pintu Mantu
print l1 [4, 2, 3]
Print l2 [1, 2, 3]
print l1 [4, 2, 3]
Print l2 [1, 2, 3]
[[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd']]
[[1, 'a'], [2, 'b'], [3, 'c']]
'''