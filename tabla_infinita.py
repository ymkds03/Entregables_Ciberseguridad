inicioMulti = int(input("Digita el inicio de la multiplicación: "))
finalMulti = int(input("Digita el final de la multiplicación: "))
Tabla_inicio = int(input("Digita el inicio de la tabla: "))
Tabla_final = int(input("Digita el final de la tabla: "))

for i in range (inicioMulti, finalMulti+1):
    print("\n")
    for j in range(Tabla_inicio, Tabla_final+1):
        
        print(f"{i} x {j} = {i*j}")