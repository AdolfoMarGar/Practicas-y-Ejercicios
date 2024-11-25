cadena = input("Introduce una cadena: ")

contLong = 0
longitud = []

for char in cadena:
    if char > "0" and char < "9":
        contLong += 1
    else:
        if contLong != 0:
            longitud.append(contLong)
            contLong = 0
            
# Agregar la última secuencia si termina con números
if contLong > 0:
    longitud.append(contLong)

print("Longitudes:", longitud)
