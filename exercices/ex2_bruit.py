import math
import matplotlib.pyplot as plt

k = 1.38e-23
B = 200e3


def kelvin(celsius: float) -> float:
    return celsius + 273.15


def main():

    celsius = [temp for temp in range(-40, 125 + 1)]
    kelvins = [kelvin(x) for x in celsius]

    watts = [k * t * B for t in kelvins]
    dbms = [10 * math.log10(w * 1e3) for w in watts]

    for i in range(len(dbms)):
        print(
            f"Temperature: {celsius[i]}°C Kelvins: {kelvins[i]} Watts: {watts[i]}W Noise: {dbms[i]}dbm"
        )

    plt.title(
        f"Niveau de bruit en dBm pour un canal GSM entre {celsius[0]}°C et {celsius[-1]}°C"
    )
    plt.xlabel("Temperature °C")
    plt.ylabel("Puissance dbm")
    plt.plot(celsius, dbms)
    plt.show()


if __name__ == "__main__":
    main()
