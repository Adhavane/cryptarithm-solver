from multiprocessing import Process
from pyswip import Prolog
import os

os.environ["SWI_HOME_DIR"] = "C:\\Program Files\\swipl"
import random
import time

def consult(file, query):
    # wait random time
    time.sleep(random.randint(1, 5))
    print(f"Consulting {file} with query {query}")
    prolog = Prolog()
    prolog.consult(file)
    print(list(prolog.query(query)))
    
    
if __name__ == "__main__":
    p1 = Process(target=consult, args=("knowledge_base1.pl", "father(michael,X)"))
    p2 = Process(target=consult, args=("knowledge_base2.pl", "father(peter,X)"))
    p2.start()
    p1.start()
    p2.join()
    p1.join()
    # consult("knowledge_base1.pl", "father(michael,X)")
