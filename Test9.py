import time

def ingresarPisoInicial():
     time.sleep(1)
     pisoInicial = int(input("Piso inicial de ejecucion: "))
     return pisoInicial

def simularElevador(arregloPisos, pisoInicio, mapaPisos):
    # Inicializar variables
    pisoActual = pisoInicio
    direction = "subiendo" if arregloPisos and arregloPisos[0] > pisoInicio else "bajando"
    stops = arregloPisos[:]
    iteration = 1

    print(f"\nArreglo de pisos: {arregloPisos}")
    print(f"Piso inicial de ejecución: {pisoInicio}")
    print(f"Pisos ingresados: {mapaPisos}")
    print(f"Sentido: {direction}\n")

    while stops:
        # Imprimir piso actual
        print(f"{iteration}. Elevador en piso {pisoActual}")
        iteration += 1

        # Actualizar dirección si es necesario
        if direction == "subiendo" and all(floor <= pisoActual for floor in stops):
            direction = "bajando"
        elif direction == "bajando" and all(floor >= pisoActual for floor in stops):
            direction = "subiendo"
        print(f"{iteration}. Elevador {direction}")
        iteration += 1

        # Determinar próximo destino según dirección
        if direction == "subiendo":
            nextPiso = min((floor for floor in stops if floor > pisoActual), default=None)
        else:  # direction == "bajando"
            nextPiso = max((floor for floor in stops if floor < pisoActual), default=None)

        # Moverse hacia el siguiente piso
        if nextPiso is not None:
            step = 1 if direction == "subiendo" else -1
            for i in range(pisoActual + step, nextPiso + step, step):
                print(f"{iteration}. Elevador en piso {i}")
                iteration += 1
            pisoActual = nextPiso

        # Parar en el piso actual
        print(f"{iteration}. Elevador se detiene -> {stops}")
        iteration += 1

        # Verificar si hay nuevos pisos ingresados en el mapa
        if pisoActual in mapaPisos:
            new_floor = mapaPisos[pisoActual]
            stops.append(new_floor)
            print(f"{iteration}. Piso ingresado {new_floor} → {stops}")
            iteration += 1

        # Eliminar piso actual de las paradas
        stops.remove(pisoActual)

    print(f"{iteration}. Elevador se detiene")


# Prueba
arregloPisos = [5, 29, 13, 10]
pisoInicial = ingresarPisoInicial()
mapaPisos = {5: 2, 29: 10, 13: 1, 10: 1}

simularElevador(arregloPisos, pisoInicial, mapaPisos)
