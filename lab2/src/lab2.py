#!/usr/bin/python3
import random
import math


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from scipy.stats import expon
from scipy.stats import gamma

def main():
    intensity = 3
    t = 4
    sims = [hpp(intensity, t) for i in range(0, 10000)]
    '''
    with open('hpp.txt', 'w') as f:
        for sim in sims:
            for t in sim:
                f.write(str(t))
                if t is not sim[-1]:
                    f.write(' ')
                else:
                    f.write('\n')
    '''
    Ns = [len(sim) - 1 for sim in sims]
    # T(N + 1) - T(N)
    Xs = [sim[-1] - sim[-2] for sim in sims]
    # T(N + 1) - t
    Ys = [sim[-1] - t for sim in sims]
    # T(N + 1)
    Zs = [sim[-1] for sim in sims]

    NsSupport = np.linspace(0, max(Ns))
    theoryNs  = plt.plot(NsSupport, gamma(4).pdf(NsSupport)) 
    diagramNs = plt.hist(Ns, 15, normed=True)
    plt.show()
    
    # actualXs  = plt.hist(Xs, 10)
    XsSupport = np.linspace(0, max(Xs))
    theoryXs  = plt.plot(XsSupport, expon().pdf(XsSupport)) 
    diagramXs = plt.hist(Xs, 15, normed=True)
    plt.show()

    YsSupport = np.linspace(0,int(max(Ys) + 1.0))
    theoryYs  = plt.plot(YsSupport, expon().pdf(YsSupport)) 
    diagramYs = plt.hist(Ys, 15, normed=True)
    plt.show()

    diagramZs = plt.hist(Zs, 10)
    plt.show()

    '''
    while True:
        continue
    '''
    
def hpp(intensity, t):
    i = 0
    T = [0]
    while T[i] <= t:
        U = random.random()
        i = i + 1
        T.append(T[i - 1] - (math.log(U) / intensity))
    return T

if __name__ == "__main__":
    main()
