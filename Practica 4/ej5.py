def getLetraDNI(num):
    letra = [
        "T",
        "R",
        "W",
        "A",
        "G",
        "M",
        "Y",
        "F",
        "P",
        "D",
        "X",
        "B",
        "N",
        "J",
        "Z",
        "S",
        "Q",
        "V",
        "H",
        "L",
        "C",
        "K",
        "E",
    ]

    return letra[num % 23]


n = int(input("Introduce los numeros de tu DNI: "))

print("Tu DNI completo es: {0}{1}".format(n, getLetraDNI(n)))
