from multiprocessing import Process, Queue, set_start_method
from pyswip import Prolog
import os
import random
import time
import pyswip
import importlib  # reload



def get_pl(q):
    prolog = Prolog()
    q.put(prolog)

if __name__ == '__main__':
    set_start_method('spawn')
    q = Queue()
    p1 = Process(target=get_pl, args=(q,))
    p1.start()
    prolog1 = q.get()
    p1.join()
    print(prolog1)
    
    p2 = Process(target=get_pl, args=(q,))
    p2.start()
    prolog2 = q.get()
    p2.join()
    print(prolog2)
    
    prolog1.consult("knowledge_base1.pl")
    print(list(prolog1.query("father(michael,X)")))
    prolog2.assertz("unload_file('knowledge_base1.pl')")
    prolog2.consult("knowledge_base2.pl")
    print(list(prolog2.query("father(peter,X)")))
