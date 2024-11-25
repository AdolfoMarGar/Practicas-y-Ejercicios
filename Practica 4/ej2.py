def esPrimo(num):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
    return primo

def primosHastaN(n):
    primos = []
    for i in range(2, n + 1):
        if esPrimo(i) == True:
            primos.append(i)
    return primos

n = int(input("Introduce un número: "))

lista = primosHastaN(n)



print("Los numeros {0} son primos.".format(lista))
