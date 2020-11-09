def reader():
    for i in range(4):
        yield '<<%s'%i

def reader_wrapper(g):
    for v in g:
        yield v

wrap = reader_wrapper(reader())
for i in wrap:
    print(i)

