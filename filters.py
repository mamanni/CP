import numpy as np
import matplotlib.pyplot as plt
from random import randrange
    
def bernoulli_filter(n):
    a = np.zeros(n)
    for k in range(n):
        a[k] = randrange(2)
    count = np.count_nonzero(a == 1)
    #print(n, count)
    return a

def sensing_matrix(m,n,filters='bernoulli'):
    A = np.zeros((m,n))
    if filters=='bernoulli':
        for i in range(m):
            A[i] = bernoulli_filter(n)
    
    return A