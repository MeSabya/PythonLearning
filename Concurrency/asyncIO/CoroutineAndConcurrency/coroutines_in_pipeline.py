# An example of broadcasting a data stream onto multiple coroutine targets.
from starting_coroutine_using_decorator import start_coroutine
# A data source.  This is not a coroutine, but it sends
# data into one (target)

import time
def follow(thefile, target):
    print("follow function ....")
    #thefile.seek(0,2)      # Go to the end of the file
    while True:
         line = thefile.readline()
         print("Reading line", line)
         if not line:
             time.sleep(0.1)    # Sleep briefly
             continue
         target.send(line)

# A filter.
@start_coroutine
def grep(pattern,target):
    while True:
        line = (yield)           # Receive a line
        print("Grep got a line", line)
        if pattern in line:
            target.send(line)    # Send to next stage   bgs vv

# A sink.  A coroutine that receives data
@start_coroutine
def printer():
    while True:
         line = (yield)
         print("Printer is printing the line",line)

# Broadcast a stream onto multiple targets
@start_coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)
if __name__ == '__main__':
    with open("access-log.txt") as f:
        follow(f, broadcast([grep('python',printer()), grep('go',printer()),
                  grep('cpp',printer())])
           )