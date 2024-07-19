import os

os.environ["SWI_HOME_DIR"] = "C:\\Program Files\\swipl"

import pyswip
import importlib  # reload

def consult(file, query):
    # wait random time
    prolog = pyswip.Prolog()
    prolog.consult(file)
    print(list(prolog.query(query)))

if __name__ == "__main__":
    importlib.reload(pyswip)
    consult("knowledge_base1.pl", "father(michael,X)")
    importlib.reload(pyswip)
    consult("knowledge_base2.pl", "father(michael,X)")
    consult("knowledge_base2.pl", "mother(8)")
