"""
Considérez les 4 codes listés dans la table suivante :

|Symbole|Code I|Code II|Code III|Code IV|
|---|----|----|----|---|
|s0 |0   |0   |0   |00 |
|s1 |10  |01  |01  |01 |
|s2 |110 |001 |011 |10 |
|s3 |1110|0010|110 |110|
|s4 |1111|0011|111 |111|
1. Lesquels de ces codes sont à décodage instantanés ?
Code I et Code IV
2. Calculer l’inégalité de Kraft-McMillan pour chacun de ces codes. Discutez les résultats en
fonctions de ceux obtenus en 1).
"""


def main():
    M = 2
    N = 5

    codes = [
        [1, 2, 3, 4, 4],
        [1, 2, 3, 4, 4],
        [1, 2, 3, 3, 3],
        [2, 2, 2, 3, 3],
    ]

    kraft = [sum(M**-l for l in code) for code in codes]

    for i, k in enumerate(kraft):
        print(f"Code {i}: Kraft {k}")


if __name__ == "__main__":
    main()
