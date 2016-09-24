#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import geom

def main():
    n = 7
    k = 2000
    m = 6000
    p = 1 / math.factorial(n)

    # writing "hist_*.txt" is broken --- don't use it!
    # lines_X = [line.strip() for line in open("hist_X.txt")]
    # lines_Y = [line.strip() for line in open("hist_Y.txt")]

    lines_X = [line for line in open("X.txt")]
    lines_Y = [line for line in open("Y.txt")]
    
    hist_X_dict, extent_X = lines_to_dict(lines_X)
    hist_Y_dict, extent_Y = lines_to_dict(lines_Y)

    hist_X = dict_to_list(hist_X_dict, extent_X)
    # hist_Y starts at i = 1: at least one trial is needed
    hist_Y = dict_to_list(hist_Y_dict, extent_Y)[1:extent_Y + 1]

    # sum(hist_X) == k;
    # to be pmf, sum(normed_hist_X) must be 1
    normed_hist_X = [x / k for x in hist_X]

    # less clear how to scale;
    # first normalize such that the maxmial value is 1
    # then note that the mode of G ~ geo(p) is always x = 1,
    # and G(x = 1) = p,
    # so hist_Y / (max(hist_Y)) * p = <= G(x) for all x
    # (in theory) '_`

    max_hist_Y = max(hist_Y)
    normed_hist_Y = [y / max_hist_Y * p for y in hist_Y]

    # the domain of bion(k,p) is [0, ∞);
    # we restrict to values or sim turned up 
    domain_theory_X = np.arange(0, extent_X + 1)
    domain_hist_X = range(0, extent_X + 1)

    theory_X = binom.pmf(domain_theory_X, m, p)

    domain_theory_Y = np.arange(1, extent_Y + 1)
    domain_hist_Y = range(1, extent_Y + 1)

    theory_Y = geom.pmf(domain_theory_Y, p)

    diagramX = plt.plot(
        domain_hist_X,
        normed_hist_X,
        'b',
        domain_theory_X,
        theory_X,
        'r'
    )

    plt.ylabel('P(X = x)')
    plt.xlabel('x')
    
    plt.show(diagramX)

    # close diagramX to continue
    
    diagramY = plt.plot(
        domain_hist_Y,
        normed_hist_Y,
        'b',
        domain_theory_Y,
        theory_Y,
        'r'
    )

    plt.ylabel('P(Y = y)')
    plt.xlabel('y')
    
    
    plt.show(diagramY)

def lines_to_dict(lines):
    d = {}
    extent = 0
    for line in lines:
        i = int(line)
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
        if i > extent:
            extent = i
    return (d, extent)
    
def pair_lines_to_dict(lines):
    d = {}
    extent = 0
    for line in lines:
        pair = line.split(' ')
        i = int(pair[0])
        value = int(pair[1])
        d[i] = value
        if i > extent:
            extent = i
    return (d, extent)

def dict_to_list(d, extent):
    l  = []
    for i in range(0, extent + 1):
        if i in d:
            l.append(d[i])
        else:
            l.append(0)
    return l

if __name__ == "__main__":
    main()
