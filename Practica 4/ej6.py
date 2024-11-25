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


def comprobarDNI(dni):
    n = ""
    letra = dni[len(dni) - 1]
    for i in range(len(dni) - 1):
        n += dni[i]

    if getLetraDNI(int(n)) == letra:
        return True
    else:
        return False


dni = input("Introduce los numeros de tu DNI: ")
if comprobarDNI(dni):
    print("El dni {0} es correcto.".format(dni))
else:
    print("El dni {0} no es correcto.".format(dni))
