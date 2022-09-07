import os
import logging
import time


def fork_instance(name):
    logging.info("Fork %s: starting", name)
    time.sleep(1)
    logging.info("Fork %s: Hello World!",name)
    time.sleep(1)
    logging.info("Fork %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    forks = list()
    for index in range(909):#max antal threads
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_instance, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(forks):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
    
    for index, fork in enumerate(children):
        os.waitpid(fork, 0)