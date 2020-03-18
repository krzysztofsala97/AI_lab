#!/usr/bin/env python

"""code template"""

import numpy as np


def main():
    P = np.array([[[0.108, 0.012], [0.072, 0.008]],
                 [[0.016, 0.064], [0.144, 0.576]]])
# Zadanie 1
    print(P)
# oś 0 - cavity, oś 1 - toothache, oś 2 - catch
# Zadanie 2
    P_toothache = np.sum(P, axis=(0, 2))
    print("P(toothache) = " + str(P_toothache))
# Zadanie 3
    P_cavity = np.sum(P, axis=(1, 2))
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
    # Reguła iloczynu
    # P(a,b) = P(a|b) * P(b)
    # Reguła Bayesa
    # P(b|a) = P(a|b) * P(b) / P(a)
    # Z tych zależności wynika, że wynika że
    # 1. P(Cav|Too,Cat) = P(Too,Cat|Cav) * P(Cav) / P(Too,Cat)
    # 2. P(Cav|Too,Cat) = P(Cav,Too,Cat) / P(Too,Cat)
    # co oznacza że pełny rozkaład uzyskuje się w następujący sposób:
    # P(Cav,Too,Cat) = P(Too,Cat|Cav) * P(Cav)
    # Z pełnego rozkładu obliczamy P(Too,Cat) sumując wzdłuż odpowiedniej osi (w tym przypadku 0)
    # Mając te wartość obliczamy P(Cav|Too,Cat) korzystając z jednej z zależności powyżej
    P_too_cat_giv_cav = P/np.reshape(P_cavity, (2, 1, 1))
    P_too_cat = np.sum((P_too_cat_giv_cav * np.reshape(P_cavity, (2, 1, 1))), axis=0)
    P_cav_giv_too_cat = P_too_cat_giv_cav * np.reshape(P_cavity, (2, 1, 1)) / P_too_cat
    print("Odp. do zadania 8 : "+str(P_cav_giv_too_cat))
    print("Prawdopodobieństwo że pacjent ma próchnicę jeśli boli go ząb i wiertło się nie zakleszczyło wynosi "+str(P_cav_giv_too_cat[0, 0, 1]))
    print("Prawdopodobieństwo że pacjent ma próchnicę jeśli boli go ząb i wiertło się zakleszczyło wynosi " + str(P_cav_giv_too_cat[0, 0, 0]))
# Zadanie 9
    # Zmienne są niezależne jeśli P(a,b) = P(a) * P(b)  czyli rożnica tych dwóch wyrażeń powinna być równa tablicy pustej
    P_toothache_catch = np.sum(P, axis=0)
    P_catch = np.sum(P, axis=(0, 1))
    iloczyn = np.reshape(P_toothache, (2, 1)) * P_catch
    print(P_toothache_catch)
    print(iloczyn)
    print("Zmienne toothache i catch nie są niezależne")
    # Zmienne są warunkowo niezalneżne jeśli P(a,b|c) = P(a|c) * P(b|c)
    P_cat_giv_cav = np.sum(P, axis=1)/np.reshape(P_cavity, (2, 1))
    iloczyn = P_cat_giv_cav * np.reshape((P_toothache_giv_cavity), (2, 2, 1))
# Zamiana osi w macierzy iloczyn wynika ze sposobu w jaki została zapisana tablica z pełnym rozkładem(tabilca P)
#   print(P_cat_giv_cav)
#    print(P_toothache_giv_cavity)
#    print(np.reshape(P_toothache_giv_cavity), (2, 2, 1))
#    print(P_toothache_giv_cavity)
#    print(P_cat_giv_cav)
    print(P_too_cat_giv_cav)
    print(iloczyn)
    print("Zmienne toothache i catch są niezależne warunkowo")

if __name__ == '__main__':
    main()
