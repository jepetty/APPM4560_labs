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
    l = 4
    m = 3
    q = m_m_1_queue(l, m, 0, 1000)
    #q = m_m_1_Jess(1000, l, m)

    # just to verify that things conform with expectation
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
    plt.show()
    
# cannibalized from lab 2. Thanky, Jess.
def hpp(intensity, t):
    i = 0
    T = [0]
    while T[i] <= t:
        U = random.random()
        i = i + 1
        T.append(T[i - 1] - (math.log(U) / intensity))
    return T

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
