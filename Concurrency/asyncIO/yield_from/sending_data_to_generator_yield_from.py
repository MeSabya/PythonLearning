def writer():
    while True:
        w = yield
        print('>>', w)

def writer_wrapper_question(coro):
    pass

'''
How a wrapper function handle sending data to the writer, so that any data that is sent to the 
wrapper is transparently sent to the writer. solution is below:
'''

def writer_wrapper_soln(coro):
    coro.send(None)      # commenting this and line below will lead to TypeError: can't send non-None value to a just-started generator
    #coro.__next__       # because coroutine started by __next__ or send(None) .
    while True:
        try:
            x = (yield)
            coro.send(x)
        except StopIteration:
            pass


'''
Instead of writing all the above code in writer_wrapper_soln how can we do the same 
using yield from 
'''
def writer_wrapper_soln_yield_from(coro):
    yield from coro

w = writer()
#wrap = writer_wrapper_soln(w)
wrap = writer_wrapper_soln_yield_from(w)
#wrap.send("sabya")  #uncommenting this will trigger TypeError: can't send non-None value to a just-started generator
wrap.send(None)
wrap.send("sabya")
for i in range(4):
    wrap.send(i)
