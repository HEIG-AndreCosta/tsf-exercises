"""
Une source émet aléatoirement un symbole parmi quatre symboles possibles. Ces quatre sym-
boles ont des probabilités d’occurrence telles que p0 = 0.4, p1 = 0.3, p2 = 0.2 et p3 = 0.1 et sont
statistiquement indépendants.
1. Calculer l’information associée à l’émission de chacun de ces 4 symboles.
2. Calculer l’entropie de la source.
"""

import math


def info(p):
    return -math.log2(p)


def main():
    """
    1. Calculer l’information associée à l’émission de chacun de ces 4 symboles.
    """
    data = [("p0", 0.4), ("p1", 0.3), ("p2", 0.2), ("p3", 0.1)]
    for name, p in data:
        print(f"{name}: P = {p} I = {info(p)}")

    """
    2. Calculer l’entropie de la source.
    """
    h = sum(p * info(p) for _, p in data)

    print(f"H = {h}")


if __name__ == "__main__":
    main()
