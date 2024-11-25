n = int(input("Introduce un numero entero: "))

igual = False
lista = []

while n != 1 and not igual:
    aux = 0
    for digit in str(n):
        aux += int(digit) ** 2
    if aux in lista:
        igual = True
    lista.append(aux)
    n = aux

if igual:
    print("No es un numero feliz")
    print(lista)
else:
    print("Es un numero feliz")
    print(lista)
