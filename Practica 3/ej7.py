continuar = True
sudoku = []
for i in range(9):
    filaAux = []
    for j in range(9):
        filaAux.append(0)
    sudoku.append(filaAux)

for linea in sudoku:
    print(linea, ",")

while continuar == True:

    fila = int(input("¿Que fila quieres cambiar? "))-1
    columna = int(input("¿Que columna quieres cambiar? "))-1
    num = int(input("¿Numero a introducir?"))
    if sudoku[fila][columna] == 0:
        sudoku[fila][columna] = num
    else:
        print("No se puede introducir ya que tiene un valor.")

    for linea in sudoku:
        print(linea, ",")

    aux = input("Deseas continuar (si/no): ")
    if aux != "si":
        continuar = False
