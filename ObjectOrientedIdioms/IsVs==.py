'''
== versus is
The == operator compares by checking equality.
Whereas, the is operator compares identities. For example, if we have two variables x and y as:

x = [1, 2, 3]
y = x
Here, the question is:
what will x == y and x is y will evaluate to?
x == y will return True because both lists look the same.
This doesn’t assure that both variables point to the same object.
To verify whether both variables hold a reference to the same object, use the is operator.
In this case, x is y will also be True because they both are pointing to one list object.
'''

# Example1
x = [1, 2, 3]
y = x

print(x == y)
print(x is y)

# Example2
x = [1, 2, 3]
y = list(x)

print(x == y)
print(x is y)
