def esPrimo(num):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
    return primo

def distanciaPrima(n):
    encontrado = False
    cont = 0

    while not encontrado:
        if esPrimo(n + cont) or (n - cont > 1 and esPrimo(n - cont)):
            encontrado = True
        else:
            cont += 1
    return cont

n = int(input("Introduce un número: "))

dPrimo = distanciaPrima(n)

print("La distancia prima de {0} es {1}".format(n, dPrimo))
