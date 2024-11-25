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


def esSemiprimo(n):
    primos = primosHastaN(n)
    i = 0
    while i < len(primos):
        j = i
        while j < len(primos):
            if primos[i] * primos[j] == n:
                return True
            j += 1
        i += 1
    return False


n = int(input("Introduce un número: "))

if esSemiprimo(n):
    aux = "si"
else:
    aux = "no"
print("El numero {0} {1} es semiprimo.".format(n, aux))
