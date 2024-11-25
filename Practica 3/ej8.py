continuar = True
sudoku = []
for i in range(9):
    filaAux = []
    for j in range(9):
        filaAux.append(0)
    sudoku.append(filaAux)

print(" ")
print(" ")
for i in range(len(sudoku)):
    if i % 3 == 0:
        print("+-------+-------+-------+")
    for j in range(len(sudoku[i])):
        if j % 3 == 0:
            print("| ", end="")
        if sudoku[i][j] == 0:
            print(". ", end="")
        else:
            print(f"{sudoku[i][j]} ", end="")
    print("|")
print("+-------+-------+-------+")

while continuar == True:
    fila = int(input("¿Que fila quieres cambiar? ")) - 1
    columna = int(input("¿Que columna quieres cambiar? ")) - 1
    num = int(input("¿Numero a introducir?"))

    if sudoku[fila][columna] == 0:
        sudoku[fila][columna] = num
    else:
        print("No se puede introducir ya que tiene un valor.")

    for i in range(len(sudoku)):
        if i % 3 == 0:
            print("+-------+-------+-------+")
        for j in range(len(sudoku[i])):
            if j % 3 == 0:
                print("| ", end="")
            if sudoku[i][j] == 0:
                print(". ", end="")
            else:
                print(f"{sudoku[i][j]} ", end="")
        print("|")
    print("+-------+-------+-------+")

    aux = input("Deseas continuar (si/no): ")
    if aux != "si":
        continuar = False
