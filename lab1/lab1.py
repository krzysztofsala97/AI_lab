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
<<<<<<< HEAD
    print("P(cavity) = " + str(P_cavity))
# zadanie 4
    P_toothache_giv_cavity = np.sum(P, axis=2)/P_cavity
    print("P(Toothache|Cavity) = " + str(P_toothache_giv_cavity))
# zadanie 5
    too_or_cat = np.sum(P, axis=(0, 1, 2)) - np.sum(P[:, 1, 1], axis=0)
    print(too_or_cat)
    P_Cav_giv_too_or_cat = (P_cavity - P[:, 1, 1])/too_or_cat
    print("P(Cavity|toothache∨catch) = " + str(P_Cav_giv_too_or_cat))
# zadanie 6
    print("Wielkość tablicy wyraża się wzorem 2^ilość_zmiennych")
# zadanie 7
    rozmiar_b = 32 * 2 ** 32
    rozmiar_B = rozmiar_b / 8
    rozmiar_KB = rozmiar_B / 1024
    rozmiar_MB = rozmiar_KB / 1024
    rozmiar_GB = rozmiar_MB / 1024
    print("Do przechowania 32 zmiennych binarnych zapisanych jako 32 bitowy float potrzeba " + str(rozmiar_GB) + "GB")
# zadanie 8
=======
    print(P_cavity)
    print("P(Toothache) wynosi " + str(P_toothache) +" a P(cavity) jest równe " + str(P_cavity))

    P_toothache_cavity = np.transpose(np.sum(P, axis=2))
    print(P_toothache_cavity)

>>>>>>> parent of 8b3fc4a... Do_zadania_5
if __name__ == '__main__':
    main()
