# coroutine.py
# A decorator function that takes care of starting a coroutine
# automatically on call.
def start_coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, *kwargs)
        cr.__next__()
        return cr
    return start

@start_coroutine
def grep(pattern):
    try:
        while True:
            print("[CO] Looking for Pattern {}".format(pattern))
            sentence = (yield)
            print("[CO] Recieved sentence {}".format(sentence))
            if pattern in sentence:
                print(sentence)
    except GeneratorExit:
        print("Received Close ..Closing Goodbye")


if __name__ == '__main__':
    g = grep('python')
    g.send("sabyasachi said: python rocks")
    g.close()