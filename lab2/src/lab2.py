#!/usr/bin/python3
import random
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

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
    print("Hmmm")
    Ns = [len(sim) - 1 for sim in sims]
    # T(N + 1) - T(N)
    Xs = [sim[-1] - sim[-2] for sim in sims]
    # T(N + 1) - t
    Ys = [sim[-1] - t for sim in sims]
    # T(N + 1)
    Zs = [sim[-1] for sim in sims]
    
    diagramNs = plt.hist(Ns, 10)
    plt.show(diagramNs)
    
    diagramXs = plt.hist(Xs, 10)
    plt.show(diagramXs)
    
    diagramYs = plt.hist(Ys, 10)
    plt.show(diagramYs)

    diagramZs = plt.hist(Zs, 10)
    plt.show(diagramZs)
    
    print("Grr")
    
def hpp(intensity, t):
    i = 0
    T = [0]
    while T[i] <= t:
        U = random.random()
        i = i + 1
        T.append(T[i - 1] - (math.log(U) / intensity))
    return T

def nhpp(C, t):
    '''
    Returns a simulated number of arrivals between time 0 and t of the nonhomogenous
    point process with intensity function y(t) = t^2 - 10t + 26
    '''
    i = 0;
    T = [0]
    while T[i] <= t:
        U1 = random.random()
        i = i + 1
        T1 = T[i - 1] - (math.log(U1)/C)
        T.append(T1)
        U2 = random.random()
        lambda_func = T1^2 - 10*T1 + 26
        if U2 > T1:
            return T
    return T

if __name__ == "__main__":
    main()
