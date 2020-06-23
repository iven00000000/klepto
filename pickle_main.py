import pickle
from random import random

class Parent2:
    def __new__(cls):
        return super().__new__(cls)

    def __init__(self):
        self.val = int(1000 * random())


with open('test_pickle_parent2.pkl', 'wb') as fp:
    p = Parent2()
    pickle.dump(p, fp)
    print(p.val)

with open('test_pickle_parent2.pkl', 'rb') as fp:
    pp = pickle.load(fp)
    print(pp.val)