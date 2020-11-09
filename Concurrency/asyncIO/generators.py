def test():
    yield "sabya 1st"
    yield "sabya 2nd"

gen = test()
print(next(gen))
print(next(gen))
#print(next(gen))

print("Now testing send and throw  ...")
'''
send and throw:
==============
We can communicate with generators using send and throw 
'''

def test_generator_communication():
    val = yield 1
    print(val)
    yield val
    yield 3

test_gen = test_generator_communication()
print(next(test_gen))
print(test_gen.send("generator value"))
print(next(test_gen))


print("Test returning values from generator")

'''
Can we use return statement in a generator ?
Yes we can use return statement but 
Returning a value from a generator, results in the value being put inside the StopIteration exception.
'''
def test_generator_ret():
    yield 1
    return "abc"

test_gen_ret = test_generator_ret()
print(next(test_gen_ret))
try:
    next(test_gen_ret)
except StopIteration as exc:
    print(exc.value)


