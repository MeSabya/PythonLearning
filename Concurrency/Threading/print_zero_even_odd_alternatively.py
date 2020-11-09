'''
This is the example to show the usage of Lock in threading ...
'''

from threading import Lock, Thread


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n

        self.zero_mutex = Lock()
        self.odd_mutex = Lock()
        self.even_mutex = Lock()

        # Lock mutex for even number and odd number,
        # because 0 must be printed first
        self.even_mutex.acquire()
        self.odd_mutex.acquire()

    def printNumber(self, num):
        print(num)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:

        for i in range(1, self.n + 1):

            # lock mutex for zero
            self.zero_mutex.acquire()

            printNumber(0)

            if (i % 2) == 1:
                # unlock mutex for odd number
                self.odd_mutex.release()
            else:
                # unlock mutex for even number
                self.even_mutex.release()
        #self.zero_mutex.release() Why we dont need this , because it would be released by even or odd thread based on input number

    def even(self, printNumber: 'Callable[[int], None]') -> None:

        for i in range(2, self.n + 1, 2):
            # lock mutex for even number
            self.even_mutex.acquire()

            printNumber(i)

            # unlock mutex for zero
            self.zero_mutex.release()
        self.even_mutex.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:

        for i in range(1, self.n + 1, 2):
            # lock mutex for odd number
            self.odd_mutex.acquire()

            printNumber(i)

            # unlock mutex for zero
            self.zero_mutex.release()
        self.odd_mutex.release()


zeroEvenOdd = ZeroEvenOdd(8)
th_zero = Thread(target=zeroEvenOdd.zero, args=(zeroEvenOdd.printNumber, ))
th_even = Thread(target=zeroEvenOdd.even, args=(zeroEvenOdd.printNumber, ))
th_odd = Thread(target=zeroEvenOdd.odd, args=(zeroEvenOdd.printNumber, ))


threads = []
threads.append(th_even)
threads.append(th_odd)
threads.append(th_zero)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
