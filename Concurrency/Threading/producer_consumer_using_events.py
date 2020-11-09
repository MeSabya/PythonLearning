import random
import threading
import concurrent.futures
import queue
import time
import logging

class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=2)

    def get_message(self, name):
        logging.debug("%s:about to get from queue", name)
        value = self.get()
        logging.debug("%s:got %d from queue", name, value)
        return value

    def set_message(self, value, name):
        logging.debug("%s:about to add %d to queue", name, value)
        self.put(value)
        logging.debug("%s:added %d to queue", name, value)

def producer(pipeline, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    logging.info("Producer received EXIT event. Exiting")

def consumer(pipeline, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info(
            "Consumer storing message: %s  (queue size=%s)",
            message,
            pipeline.qsize(),
        )

    logging.info("Consumer received EXIT event. Exiting")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()

'''
OUTPUT:
00:10:06: Producer got message: 28   # 
00:10:06: Producer got message: 92
00:10:06: Producer got message: 64    # Here producer pushed 3 messages 
00:10:06: Consumer storing message: 28  (queue size=1)  # But after consuming 1 message queue size is 1 , should be 2
00:10:06: Consumer storing message: 92  (queue size=0)
00:10:06: Producer got message: 35
00:10:06: Producer got message: 87
00:10:06: Consumer storing message: 64  (queue size=1)
00:10:06: Producer got message: 91
00:10:06: Consumer storing message: 35  (queue size=1)
00:10:06: Producer got message: 55
00:10:06: Consumer storing message: 87  (queue size=1)
00:10:06: Producer got message: 68
00:10:06: Consumer storing message: 91  (queue size=1)

***** Deleted so many lines in mid *****
00:10:06: Main: about to set event
00:10:06: Consumer storing message: 93  (queue size=0)
00:10:06: Producer got message: 9
00:10:06: Consumer storing message: 62  (queue size=0)
00:10:06: Producer received EXIT event. Exiting
00:10:06: Consumer storing message: 9  (queue size=0)
00:10:06: Consumer received EXIT event. Exiting

Process finished with exit code 0

'''