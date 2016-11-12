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
    while True:
        continue
    
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
