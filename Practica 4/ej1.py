def esPrimo(num):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
    return primo


n = int(input("Introduce un número: "))
if esPrimo(n) == True:
    aux = "si"
else:
    aux = "no"

print("El numero {0} {1} es primo".format(n, aux))
