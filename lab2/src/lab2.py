#!/usr/bin/python3
import random
import math


import numpy as np
import scipy as sci
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import scipy.stats as stats

# from scipy.stats import expon
# from scipy.stats import gamma
# from scipy.stats import poisson

def main():
    # print(sci.__version__)
    #simulate_hpp()
    simulate_nhpp()

def simulate_nhpp():
    t = 9
    # max value of our lambda function occurs at x = 0, lambda = 26
    C = 26
    sims = [nhpp(C,t) for i in range (0, 10000)]

    Ns = [len(sim) - 2 for sim in sims]
    average = sum(i for i in Ns)/10000
    print("Simulated value of W: ", average)

    diagramNs = plt.hist(Ns, 10)
    plt.title("Simulations of $N$ over $[0,9]$ for NHPP($\lambda(t)=t^2 - 10t + 26$)")
    plt.xlabel("$N$")
    plt.ylabel("Count of $N$")
    plt.show(diagramNs)

def simulate_hpp():
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
    Ns = [len(sim) - 2 for sim in sims]
    average = sum(i for i in Ns)/10000
    print("Simulated value of N: ", average)
    # T(N + 1) - T(N)
    Xs = [sim[-1] - sim[-2] for sim in sims]
    # T(N + 1) - t
    Ys = [sim[-1] - t for sim in sims]
    # T(N + 1)
    Zs = [sim[-1] for sim in sims]

    NsSupport = np.arange(0,max(Ns))
    theoryNs = plt.plot(NsSupport, stats.poisson.pmf(NsSupport, mu=12))
    diagramNs = plt.hist(Ns, normed=True,color='r')
    plt.title("Simulations of $N$ over $[0,4]$ for HPP(3)")
    plt.xlabel("$N$")
    plt.ylabel("Count of $N$")
    plt.show()

    XsSupport = np.linspace(0, max(Xs))
    theoryXs  = plt.plot(XsSupport, stats.expon.pdf(XsSupport,loc=0,scale=1/3)) 
    diagramXs = plt.hist(Xs, normed=True,color='r')
    plt.title("Simulations of $T(N+1) - T(N)$ over $[0,4]$ for HPP(3)")
    plt.xlabel("$T(N+1) - T(N)$")
    plt.ylabel("Count of $T(N+1) - T(N)$")
    plt.show()
    
    YsSupport = np.linspace(0,max(Xs))
    theoryYs  = plt.plot(YsSupport, stats.expon.pdf(YsSupport,loc=0,scale=1/3))
    diagramYs = plt.hist(Ys, normed=True,color='r')
    plt.title("Simulations of $T(N+1) - t$ over $[0,4]$ for HPP(3)")
    plt.xlabel("$T(N+1) - t$")
    plt.ylabel("Count of $T(N+1) - t$")
    plt.show()

    ZsSupport = np.linspace(4.0, max(Zs))
    # theoryZs  = plt.plot(ZsSupport, gamma(4).pdf(ZsSupport))
    theoryZs = plt.plot(ZsSupport, stats.expon.pdf(ZsSupport,loc=4,scale=1/3))
    diagramZs = plt.hist(Zs, normed=True,color='r')
    plt.title("Simulations of $T(N+1)$ over $[0,4]$ for HPP(3)")
    plt.xlabel("$T(N+1)$")
    plt.ylabel("Count of $T(N+1)$")
    plt.show()

def hpp(intensity, t):
    i = 0
    T = [0]
    while T[i] <= t:
        U = random.random()
        i = i + 1
        T.append(T[i - 1] - (math.log(U) / intensity))
    return T

def nhpp(C, tn):
    '''
    Returns a simulated number of arrivals between time 0 and t of the nonhomogenous
    point process with intensity function y(t) = t^2 - 10t + 26
    '''
    i = 0
    T = [0]
    lambda_func = 0
    U2 = 0
    while T[i] <= tn:
        U1 = random.random()
        T1 = T[i] - (math.log(U1)/C)
        U2 = random.random()
        lambda_func = (T1*T1 - 10*T1 + 26)/C
        if (U2 <= lambda_func):
            i = i + 1
            T.append(T1)
    return T

if __name__ == "__main__":
    main()
