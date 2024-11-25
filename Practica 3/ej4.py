p1 = input("Introduce la palabra 1: ")

seguir = True
while seguir:
    p2 = input("Introduce la siguiente palabra: ")

    # Comienza desde el final de p1 y el inicio de p2
    for i in range(1, len(p2) + 1):
        if p1[-i:] == p2[:i]:
            coinciden = i

    print(f"'{p1}' y '{p2}' enlazan con {coinciden} letras.")
    if coinciden < 2:
        seguir = False
    p1 = p2
