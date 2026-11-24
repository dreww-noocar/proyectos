def main():
    #----variables principales-----

    lista_maquinas = []
    mediciones = []

    #----definicion de funciones-----

    def buscar_maquina(lista_maquinas, clave):
    
            for i in range(len(lista_maquinas)):
    
                if lista_maquinas[i]["identificador"] == clave:
                    return i
    
            return -1

    def validar_numero(numero):
        try:
            numero = float(numero)

            if numero < -50 or numero > 200:
                return False

            return True

        except ValueError:
            return False

    
    def agregar_maquinas(lista_maquinas, mediciones):

        agg_maquinas = int(input("ingresa la cantidad de maquinas a agregar: "))

        for i in range(agg_maquinas):
            print(f"=========maquina {i + 1}=========")

            clave = input("clave de la maquina (no repetir claves): ").strip().upper()

            while (len(clave) < 1 or len(clave) > 10 or buscar_maquina(lista_maquinas, clave) != -1 or not clave.isalnum()):
                print("=========la clave debe tener entre 1 y 10 caracteres ademas de no ser repetida=========")
                clave = input("clave de la maquina (no repetir claves): ").strip().upper()

            nombre = input("nombre: ").strip()

            while len(nombre) < 1 or len(nombre) > 20:
                print("=========el nombre debe tener entre 1 y 20 caracteres=========")
                nombre = input("nombre: ").strip()

            ubicacion = input("ubicacion: ").strip()

            while len(ubicacion) < 1 or len(ubicacion) > 20:
                print("=========la ubicacion debe tener entre 1 y 20 caracteres=========")
                ubicacion = input("ubicacion: ").strip()

            minimo = (input("temperatura minima: "))

            while not validar_numero(minimo):
                print("=========ingresa un numero valido=========")
                minimo = (input("temperatura minima: "))

            minimo = float(minimo)

            maximo = (input("temperatura maxima: "))

            while not validar_numero(maximo):
                print("=========ingresa un numero valido=========")
                maximo = (input("temperatura maxima: "))
                
            maximo = float(maximo)

            while minimo >= maximo:
                print("=========la temperatura minima debe ser menor a la maxima=========")
                minimo = (input("temperatura minima: "))

                while not validar_numero(minimo):
                    print("=========ingresa un numero valido=========")
                    minimo = (input("temperatura minima: "))

                minimo = float(minimo)

                maximo = (input("temperatura maxima: "))

                while not validar_numero(maximo):
                    print("=========ingresa un numero valido=========")
                    maximo = (input("temperatura maxima: "))
                    
                maximo = float(maximo)

            maquina = {
                "identificador": clave,
                "nombre": nombre,
                "ubicacion": ubicacion,
                "variable": "Temperatura de operacion",
                "unidad": "°C",
                "limites": (minimo, maximo)
            }

            lista_maquinas.append(maquina)
            mediciones.append([None, None, None, None, None])

            print(f"=========maquina {i + 1} agregada=========")

    def agregar_mediciones(lista_maquinas, mediciones):

        if len(lista_maquinas) == 0:
            print("=========no hay maquinas registradas=========")
            return

        input_clave = buscar_maquina(lista_maquinas, input("ingresa la clave de la maquina: ").strip().upper())

        if input_clave == -1:
            print("=========la maquina no existe=========")
            return

        if mediciones[input_clave][0] is not None:
            opcion = input("=========ya se han registrado mediciones para esta maquina. Quieres cambiarlas? (s/n): ========").strip().lower()

            while opcion != 's' and opcion != 'n':
                print("=========ingrese una opcion valida=========")
                opcion = input("=========ya se han registrado mediciones para esta maquina. Quieres cambiarlas? (s/n): ========").strip().lower()

            if opcion == 'n':
                return

        temperaturas = []

        for i in range(5):
            print(f"=========medicion {i + 1}=========")

            temperatura = (input("introduce la medicion: "))

            while not validar_numero(temperatura):
                print("=========ingresa un numero valido=========")
                temperatura = (input("introduce la medicion: "))

            temperaturas.append(float(temperatura))

        mediciones[input_clave] = temperaturas

    def cambiar_limites(lista_maquinas):

        if len(lista_maquinas) == 0:
            print("=========no hay maquinas registradas=========")
            return

        input_clave = buscar_maquina(lista_maquinas, input("ingresa la clave de la maquina: ").strip().upper())

        if input_clave == -1:
            print("=========la maquina no existe=========")
            return

        minimo = (input("temperatura minima: "))
        
        while not validar_numero(minimo):
            print("=========ingresa un numero valido=========")
            minimo = (input("temperatura minima: "))
        
        minimo = float(minimo)
        
        maximo = (input("temperatura maxima: "))
        
        while not validar_numero(maximo):
            print("=========ingresa un numero valido=========")
            maximo = (input("temperatura maxima: "))
                        
        maximo = float(maximo)
        
        while minimo >= maximo:
            print("=========la temperatura minima debe ser menor a la maxima=========")
            minimo = (input("temperatura minima: "))
        
            while not validar_numero(minimo):
                print("=========ingresa un numero valido=========")
                minimo = (input("temperatura minima: "))
        
            minimo = float(minimo)
        
            maximo = (input("temperatura maxima: "))
        
            while not validar_numero(maximo):
                print("=========ingresa un numero valido=========")
                maximo = (input("temperatura maxima: "))
                            
            maximo = float(maximo)

        lista_maquinas[input_clave]["limites"] = (minimo,maximo)

    def analisis_mediciones(lista_maquinas, mediciones):

        clave = input("ingresa la clave de la maquina: ").strip().upper()
        
        input_clave = buscar_maquina(lista_maquinas, clave)

        if input_clave == -1:
            print("=========la maquina no existe=========")
            return

        if None in mediciones[input_clave]:
            print("=========no se han registrado mediciones para esta maquina=========")
            return

        min, max = lista_maquinas[input_clave]["limites"]

        analisis = {
            "identificador": (lista_maquinas[input_clave]["identificador"]),
            "Nombre": (lista_maquinas[input_clave]["nombre"]),
            "ubicacion": (lista_maquinas[input_clave]["ubicacion"]),
            "variable": "temperatura de operacion",
            "rango de operacion": (min, max),
            "mediciones": "sin mediciones",
            "promedio": "sin mediciones",
            "minima observada": "sin mediciones",
            "maxima observada": "sin mediciones",
            "R1": "sin mediciones",
            "R2": "sin mediciones",
            "R3": "sin mediciones",

        }

        

    
main()