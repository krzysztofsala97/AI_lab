#!/usr/bin/env python

"""code template"""

import numpy as np


def main():
# zadanie 1
    P = np.array([[[0.108, 0.012], [0.072, 0.008]],
                 [[0.016, 0.064], [0.144, 0.576]]])
    print(P)
# oś 0 - cavity, oś 1 - toothache, oś 2 - catch
# zadanie 2
    P_toothache = np.sum(P, axis=(0, 2))
    print("P(Toothache)= " + str(P_toothache))
# zadanie 3
    P_cavity = np.sum(P, axis=(1, 2))
    print("P(cavity) = " + str(P_cavity))
# zadanie 4
    P_toothache_giv_cavity = np.sum(P, axis=2)/P_cavity
    print("P(Toothache|Cavity) = " + str(P_toothache_giv_cavity))
# zadanie 5
    
if __name__ == '__main__':
    main()
