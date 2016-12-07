#!/usr/bin/python3
import random
import math

def main():
    m_m_1_queue(1,1,0,10)
    print "Je n'ai rien d'idee ce dont je vais tenter."
    print "Badoinkanwellen wirken wie Badoinkanpartikel. Auch geil!"
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
    Input: (lambda, mu, n) where
       * lambda: intensity param for hpp arrivals
       * mu: rate param for exponential service
       * n: number of clients at time t = 0
       * T: fixed time to which the M/M/1 is simulated
    Output: tau-sorted arrivals list pairs where for pairs[i] = (tau, i)
       * tau for 0 < tau < T  is the time of ith queue event
       * y = +1 if the t = tau event is an arrival; y = -1 if it's a departure
'''
def m_m_1_queue(lambda, mu, n, T):
    t, i, tau, y = 0
    q = [0]
    while q[i][0] <= T:
        U = random.random()
        i = i + 1
        if n is 0:
            '''
            items can only be enqueed if empty;
            arrive w/ intensity lambda
            '''
            tau = (q[i - 1][0] - (math.log(U) / lambda))
            y = 1
        else:
            '''
            if non-empty, clients can either arrive or leave;
            use superposition argument to get
              higher-rate event times;
            use thinning argument to select whether event
              is arrival or departure
            '''
            tau = (q[i - 1][0] - (math.log(U) / (lambda + mu)))
            U_increment = random.random()
            if U_increment <= lambda / (lambda + mu):
                # w/ prob lambda / (lambda + mu), an arrival
                y = +1
            else:
                # else, a departure
                y = -1
        q.append((tau, y))
    return T

if "__name__" == __main__:
    main()
