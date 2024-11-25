baraja = []
for c in ["azul", "verde", "rojo", "amarillo"]:
    cont = 0
    baraja.append("0, " + c)
    while cont < 2:
        for i in range(9):
            baraja.append("{0}, {1}".format(i + 1, c))
        for tipo in ["roba2", "reversa", "salta"]:
            baraja.append("{0}, {1}".format(tipo, c))

        cont += 1
    baraja.append("Comodin, None")
    baraja.append("Roba4, None")

print(baraja)
