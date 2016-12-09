#!/usr/bin/python3

import math
import random

import numpy as np
import scipy as sci
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import scipy.stats as stats
import collections

def main():
    l = 1
    m = 2
    T = 50
    simulate_part2(l, m, T)
    simulate_part3(l, m, T)
    simulate_part4(l, m, T)

    #q = m_m_1_queue(l, m, 0, T)
    #find_inter_departure(q)
    #q = m_m_1_Jess(T, l, m)

    # just to verify that things conform with expectation
    '''
    ns = [event[2]  for event in q]
    max_n = max(ns)
    sigma = sum(ns)
    print(sigma)
    ns_counter = collections.Counter(ns)
    pi = [float(ns_counter[i]) / float(sigma) for i in range(0, max_n + 1)]
    diagram_support = range(1, max_n + 1)
    diagram = plt.hist(ns, normed=True, color='r', align='left', bins = diagram_support)
    theory_support = np.arange(1, max(ns) + 1)
    theory = plt.plot(theory_support, stats.geom.pmf(theory_support, m / l))
    plt.show()'''

def simulate_part2(l, m, T): 
    sims = []
    for i in range(0,10000):
        n = simulate_n(l, m)
        q = m_m_1_queue(l, m, n, T)
        sims.append(calculate_Xt(q, n))
    diagram_support = range(1, max(sims) + 1)
    diagram = plt.hist(sims, normed=True, color='r', align='left', bins=diagram_support)
    theory_support = np.arange(1, max(sims)+1)
    theory = plt.plot(theory_support, stats.geom.pmf(theory_support, l/m))
    axes = plt.gca()
    axes.set_xlim(1, max(sims))
    plt.title("Simulations of $X_T$ with $(\lambda, \mu, T) = (1,2,50)$")
    plt.xlabel("$n$ number of items in queue at time $T$")
    plt.ylabel("Proportion of time with $n$ items")
    plt.show()

def simulate_part3(l, m, T):
    sims = []
    for i in range(0,10000):
        n = simulate_n(l,m)
        q = m_m_1_queue(l, m, n, T)
        sims.append(calculate_frac(q, n, T))
    diagram = plt.hist(sims, normed=True, color='r', align='left')
    plt.title("Simulations of Percent of Time the Server is Busy")
    plt.xlabel("Percent of time the server is busy")
    plt.ylabel("Proportion of simulations")
    plt.show()

def simulate_part4(l, m, T):
    sims = []
    for i in range(0, 10000):
        n = simulate_n(l, m)
        q = m_m_1_queue(l, m, n, T)
        sims.append(find_inter_departure(q))
        #print(find_inter_departure(q))
    # jacked analysis code for HPP from lab 2 thx
    Ns = [len(sim) - 1 for sim in sims]
    Xs = [sim[-1] - sim[-2] for sim in sims]
    Ys = [T - sim[-1] for sim in sims]
    Zs = [sim[-1] for sim in sims]

    NsSupport = np.arange(0, max(Ns))
    theoryNs = plt.plot(NsSupport, stats.poisson.pmf(NsSupport, mu=50))
    diagramNs = plt.hist(Ns, normed=True, color='r')
    plt.title("Simulations of $N(t)$ for HPP(1) over $[0, T=50]$")
    plt.xlabel("$N(t)$")
    plt.ylabel("Count of $N(t)$")
    plt.show()

    XsSupport = np.linspace(0, max(Xs))
    theoryXs = plt.plot(XsSupport, stats.expon.pdf(XsSupport, loc=0, scale=1/3))
    diagramXs = plt.hist(Xs, normed=True, color='r')
    plt.title("Simulations of $T(N+1) - T(n)$ for HPP(1) over $[0, T=50]$")
    plt.xlabel("$T(n) - T(n-1)$")
    plt.ylabel("Count of $T(n+1) - T(n)$")
    plt.show()

    YsSupport = np.linspace(0, max(Ys))
    theoryYs = plt.plot(YsSupport, stats.expon.pdf(YsSupport, loc=0, scale=1/3))
    diagramYs = plt.hist(Ys, normed=True, color='r')
    plt.title("Simulations of $T - T(n)$ for HPP(1) over $[0, T=50]$")
    plt.xlabel("$T - T(n)$")
    plt.ylabel("Count of $T - T(n)$")
    plt.show()

    ZsSupport = np.linspace(50, max(Zs))
    theoryZs = plt.plot(ZsSupport, stats.expon.pdf(ZsSupport, loc=50, scale=1/3))
    diagramZs = plt.hist(Zs, normed=True, color='r')
    plt.title("Simulations of $T(n)$ for HPP(1) over $[0, T=50]$")
    plt.xlabel("$T(n)$")
    plt.ylabel("Count of $T(n)$")
    plt.show()

def calculate_frac(q, n, T):
    t = 0
    if n == 0:
        t = t + q[1][0]
        q = q[1:]
    for i in range(len(q)):
        n = n + q[i][1]
        if n == 0:
            if (i < len(q) - 1):
                t = t + (q[i+1][0] - q[i][0])
            else:
                t = t + (T - q[i][0])
    return (T-t)/T

def find_inter_departure(q):
    first = 0
    i = 0
    times = []
    '''while first == 0:
        if q[i][1] == -1:
            first = q[i][0]
        i = i + 1
    for i in range(i, len(q)):
        if q[i][1] == -1:
            times.append(q[i][0] - first)
            first = q[i][0]
    return times'''
    for i in range(len(q)):
        if q[i][1] == -1:
            times.append(q[i][0])
    return times


def simulate_n(l,m):
    u = random.random()
    i = 0
    x = (1 - l/m)*(l/m)**i
    while (u > x):
        i = i + 1
        x = x + (1 - l/m)*(l/m)**i
    return i
    
# cannibalized from lab 2. Thanky, Jess.
def hpp(intensity, t):
    i = 0
    T = [0]
    while T[i] <= t:
        U = random.random()
        i = i + 1
        T.append(T[i - 1] - (math.log(U) / intensity))
    return T

def calculate_Xt(q, n):
    for i in range(len(q)):
        n = n + q[i][1]
    return n

'''
    Input: (l, mu, n) where
       * l: intensity param for hpp arrivals
       * mu: rate param for exponential service
       * n: number of clients at time t = 0
       * T: fixed time to which the M/M/1 is simulated
    Output: tau-sorted arrivals list pairs where for pairs[i] = (tau, i)
       * tau for 0 < tau < T  is the time of ith queue event
       * y = +1 if the t = tau event is an arrival; y = -1 if it's a departure
'''
def m_m_1_queue(l, mu, n, T):
    #t = 0
    i = 0
    tau = 0
    y = 0
    q = [(0, 0, 0)]
    while q[i][0] <= T:
        U = random.random()
        i = i + 1
        if n is 0:
            '''
            items can only be enqueed if empty;
            arrive w/ intensity l
            '''
            tau = (q[i - 1][0] - (math.log(U) / l))
            y = 1
        else:
            '''
            if non-empty, clients can either arrive or leave;
            use superposition argument to get
              higher-rate event times;
            use thinning argument to select whether event
              is arrival or departure
            '''
            tau = (q[i - 1][0] - (math.log(U) / (l + mu)))
            U_increment = random.random()
            if U_increment <= (l / (l + mu)):
                # w/ prob l / (l + mu), an arrival
                y = +1
            else:
                # else, a departure
                y = -1
        n += y
        q.append((tau, y, n))
    return q[1:-1]

def m_m_1_Jess(T, l, m):
    t = 0
    D  = []
    A  = []
    AD = []
    n = 0
    r_1 = -math.log(random.random()) / l
    t += r_1
    while t <= T:
        A.append(t)
        n = n + 1
        AD.append((t,1,n))
        r_1 = -math.log(random.random()) / l
        t = t + r_1
    r_2 = -math.log(random.random()) / m
    t = r_2
    while t < T:
        D.append(r_2)
        r_2 = - math.log(random.random()) / m
        t = t + r_2
    i_arr = 0
    i_dep = 0
    d = A[0] + D[0]
    while d < T:
        i_arr = i_arr + 1
        i_dep = i_dep + 1
        if (i_arr >= len(A)) or (i_dep >= len(D)):
            return AD
        n = n - 1
        AD.append((d,-1,n))
        if d + D[i_dep] > A[i_arr]:
            d = d + D[i_dep]
        elif d + D[i_dep] < A[i_arr]:
            d = A[i_arr] + D[i_dep]
    return AD



    # At this point I got confuzzled *~* help jess

if __name__ == "__main__":
    main()
