"""
Soit p la probabilité d’un événement, tracer la valeur de la quantité d’information relative à
l’événement en fonction de p pour 0 ≤ p ≤ 1
"""

import matplotlib.pyplot as plt
import math


def main():

    x = [p / 100 for p in range(1, 110, 10)]
    y = [-math.log2(xi) for xi in x]

    plt.plot(x, y, "blue", label="Min Obstructions")

    plt.ylabel("I")
    plt.xlabel("P")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
