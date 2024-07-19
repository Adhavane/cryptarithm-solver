
import os

os.environ["SWI_HOME_DIR"] = "C:\\Program Files\\swipl"
from multiprocessing import Process, Queue
from pyswip import Prolog
import random
import time

def worker(queue, err):
    try:
        1/0
        liste = [1, 2, 3, 4, 5]
        for i in liste:
            queue.put(i)
            time.sleep(random.random())
        queue.put(None)
    except Exception as e:
        queue.put(None)
        err.put(e)

def gen():
    # Open a new process with a queue
    # yield the queue
    
    queue = Queue()
    err = Queue()
    p = Process(target=worker, args=(queue, err))
    p.start()
    while True:
        item = queue.get()
        if item is None:
            break
        yield item
    p.join()
    if not err.empty():
        raise err.get()
    
if __name__ == "__main__":
    gen = gen()
    print(gen)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))