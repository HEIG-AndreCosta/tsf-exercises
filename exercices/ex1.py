"""
Plotter la puissance reçue (dBm) pour un Wifi à
5.8GHz en fonction de la distance pour un canal
intérieur avec des obstacles. La puissance d’émission
est de 14dBm et les antennes sont
omnidirectionnelles.
"""

import matplotlib.pyplot as plt
import math

FREQ = 5.8e9
PT = 14
GT = 1
GR = 1
SPEED_OF_LIGHT = 300e6
L = SPEED_OF_LIGHT / FREQ

OBSTRUCTION_MIN = 4
OBSTRUCTION_MAX = 6


def main():

    distances = [2**i for i in range(0, 10)]
    dbs = [
        [
            10
            * math.log10(
                PT * GT * GR * L / (((4 * math.pi) ** 2) * (distance**obstruction))
            )
            for distance in distances
        ]
        for obstruction in [OBSTRUCTION_MIN, OBSTRUCTION_MAX]
    ]

    plt.plot(distances, dbs[0], "blue", label="Min Obstructions")
    plt.plot(distances, dbs[1], "green", label="Max Obstruction")

    plt.ylabel("dBm")
    plt.xlabel("meters")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
