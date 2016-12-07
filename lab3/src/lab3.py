#!/usr/bin/python3
import random
import math

def main():
    print(m_m_1_queue(1, 1, 0, 10))

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
    t = 0
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
            print("Rand: " + str(U_increment))
            if U_increment <= (l / (l + mu)):
                # w/ prob l / (l + mu), an arrival
                y = +1
            else:
                # else, a departure
                y = -1
        n += y
        q.append((tau, y, n))
    return q[1:-1]

if __name__ == "__main__":
    print("Hey")
    main()
