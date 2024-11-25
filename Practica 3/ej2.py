sufix = input("Introduce el sufijo a comprobar: ")
palabra = input("Introduce la palabra padre: ")
cont = len(sufix) - 1
sufijo = True


for i in range(len(palabra) - 1, len(palabra) - len(sufix) - 1, -1):
    if palabra[i] != sufix[cont]:
        sufijo = False

    if cont > 0:
        cont -= 1

if sufijo:
    print(f"'{sufix}' es un sufijo de '{palabra}'.")
else:
    print(f"'{sufix}' no es un sufijo de '{palabra}'.")
