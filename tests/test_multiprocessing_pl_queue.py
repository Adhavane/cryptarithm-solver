
import os

os.environ["SWI_HOME_DIR"] = "C:\\Program Files\\swipl"
from multiprocessing import Process, Queue
from pyswip import Prolog
import random
import time

def worker(queue, err, a):
    try:
        prolog = Prolog()
        prolog.consult("knowledge_base"+str(a)+".pl")
        for soln in prolog.query("mother(8)"):
            queue.put(soln)
            time.sleep(random.random())
        queue.put(None)
    except Exception as e:
        queue.put(None)
        err.put(e)

def gen(a):
    # Open a new process with a queue
    # yield the queue
    
    queue = Queue()
    err = Queue()
    p = Process(target=worker, args=(queue, err, a))
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
    gen1 = gen(1)
    gen2 = gen(2)
    # print(gen1)
    print(next(gen1))
    print(next(gen2))
    # print(next(gen2))
    # print(next(gen1))
    # print(next(gen1))
    # print(next(gen1))
    # print(next(gen1))