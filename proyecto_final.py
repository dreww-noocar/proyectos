lista_maquinas = []
mediciones = []


agg_maquinas = int(input("ingresa la cantidad de maquinas a agregar: "))

# ===========informacion de cada maquina==========
for i in range(agg_maquinas):
    print(f"=========maquina {i + 1}=========")

    clave = input("clave de la maquina (no repetir claves): ")
    while (
        len(clave) < 1
        or len(clave) > 10
        or clave in [maquina["identificador"] for maquina in lista_maquinas]
    ):
        print(
            "=========la clave debe tener entre 1 y 10 caracteres ademas de no ser repetida========="
        )
        clave = input("clave de la maquina (no repetir claves): ")

    nombre = input("nombre: ")
    while len(nombre) < 1 or len(nombre) > 20:
        print("=========el nombre debe tener entre 1 y 20 caracteres=========")
        nombre = input("nombre: ")

    ubicacion = input("ubicacion: ")
    while len(ubicacion) < 1 or len(ubicacion) > 20:
        print("=========la ubicacion debe tener entre 1 y 20 caracteres=========")
        ubicacion = input("ubicacion: ")

    minimo = float(input("temperatura minima: "))
    maximo = float(input("temperatura maxima: "))
    while maximo < minimo or minimo < -50 or maximo > 200:
        print(
            "=========la temperatura maxima debe ser mayor a la minima y deben estar entre -50 y 200========="
        )
        minimo = float(input("temperatura minima: "))
        maximo = float(input("temperatura maxima: "))

    temperaturas = []
    for _ in range(5):
        temp = float(
            input(
                f"introduce la medicion de temperatura {_ + 1} (deben de ser 5, en orden cronologico): "
            )
        )
        while temp < -50 or temp > 200:
            print("=========la temperatura debe estar entre -50 y 200=========")
            temp = float(
                input(
                    f"introduce la medicion de temperatura {_ + 1} (deben de ser 5, en orden cronologico): "
                )
            )
        temperaturas.append(temp)
    mediciones.append(temperaturas)

    maquina = {
        "identificador": clave,
        "nombre": nombre,
        "ubicacion": ubicacion,
        "limites": (minimo, maximo),
    }

    lista_maquinas.append(maquina)
    print(lista_maquinas, mediciones)
