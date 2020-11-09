def grep(pattern):
    while True:
        print("[CO] Looking for Pattern {}".format(pattern))
        sentence = (yield)
        print("[CO] Recieved sentence:: {}".format(sentence))
        if pattern in sentence:
            print(sentence)

if __name__ == '__main__':
    g = grep('python')
    g.__next__()  # With out next co-routine will not start
    #g.send(None) # Eiether call  __next__ or send(None) to start the coroutine
    print("[MAIN] Sending the sentences")
    g.send("A Sentence will not going to be printed")
    g.send("python rocks: This will be printed")
