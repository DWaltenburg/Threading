import threading
import logging
import time


def thread_instance(name):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    logging.info("Thread %s: Hello World!",name)
    time.sleep(1)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()
    for index in range(5):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_instance, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)