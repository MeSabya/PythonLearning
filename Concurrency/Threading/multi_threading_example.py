import threading
import time

# This is an example of class inherited from thread class
class MyThread(threading.Thread):
    def run(self) -> None:
        print("{} started".format(self.getName()))
        time.sleep(1)
        print("{} Finished".format(self.getName()))

def Main():
    for x in range(4):
        mythread = MyThread(name="Thread-{}".format(x+1))
        mythread.start()

if __name__ == '__main__':
    Main()
