class iterator:
    def __init__(self):
        self.count = -1
    def __iter__(self):
        return self
    def next(self):
        self.count +=1
        if self.count < 4:
            return self.count
        else:
            return StopIteration

def loop_iterator():
    return iterator()

itr = loop_iterator()
try:
    print(itr.next())
    print(itr.next())
    print(itr.next())
    print(itr.next())
    print(itr.next())
    print(itr.next())
except StopIteration:
    print("Stop iteration")
    exit()


def some_function():
    for i in range(4):
        yield i

mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)

for i in mygenerator:
    print(i)

print("######## Testing some function #######")
ty = some_function()

for i in ty:
    print(i)


for i in ty:
    print(i)
