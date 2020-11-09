from threading import Semaphore, Barrier,Thread
class H2O:
    def __init__(self):
        self.h_semaphore = Semaphore(2)
        self.o_semaphore = Semaphore(1)
        self.barrier = Barrier(3)

    def releaseHydrogen(self):
        print('H')

    def releaseOxygen(self):
        print('O')

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.h_semaphore:
            self.barrier.wait()
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.o_semaphore:
            self.barrier.wait()
            releaseOxygen()

threads = []
create_h2o = H2O()
hydrogen_count = int(input("Enter a even number "))  # This should not be a odd number
for hc in range(hydrogen_count):
    threads.append(Thread(target=create_h2o.hydrogen,args=(create_h2o.releaseHydrogen,)))
    threads[-1].start()

oxygen_count = int(hydrogen_count/2)   # this should be half as hydrogen_count
for oc in range(oxygen_count):
    to = Thread(target=create_h2o.oxygen, args=(create_h2o.releaseOxygen,))
    threads.append(to)
    threads[-1].start()

for thread in threads:  # Waits for threads to complete before moving on with the main script.
    thread.join()

