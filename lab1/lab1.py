#!/usr/bin/env python

"""code template"""

import numpy as np


def main():
    P = np.array([[[0.108, 0.012], [0.072, 0.008]],
                 [[0.016, 0.064], [0.144, 0.576]]])
    print(P)

    P_toothache = np.sum(P, axis=(0, 2))
    print(P_toothache)
    P_cavity = np.sum(P, axis=(1, 2))
    print(P_cavity)
    print("P(Toothache) wynosi " + str(P_toothache) +" a P(cavity) jest równe " + str(P_cavity))

    P_toothache_cavity = np.transpose(np.sum(P, axis=2))
    print(P_toothache_cavity)

if __name__ == '__main__':
    main()
