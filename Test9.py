import time

def ingresarPisoInicial():
     time.sleep(1)
     pisoInicial = int(input("Piso inicial de ejecucion: "))
     return pisoInicial

#currentpos, dado, num_turno
def simularElevador(mapaPisos, initial_floor, input_floors):
    current_floor = initial_floor
    direccion = "up"
    pending_floors = mapaPisos

    def actualizarPiso(current, input_floors, pending):
        if current in input_floors:
            new_floor = input_floors[current]
            print(f"Piso ingresado: {new_floor}")
            pending.append(new_floor)
        return pending

    while pending_floors:
        print(f"\nElevador en piso: {current_floor}")
        if direccion == "up":
            # Encontrar el siguiente piso hacia arriba
            print("Elevador subiendo")
            next_stop = next((f for f in pending_floors if f >= current_floor), None)
            if next_stop is not None:
                current_floor = next_stop
                pending_floors.remove(next_stop)
                print(f"Elevador se detiene -> {pending_floors}")
                pending_floors = actualizarPiso(current_floor, input_floors, pending_floors)
            else:
                direccion = "down"
                print("Elevador descendiendo")
        elif direccion == "down":
            # Encontrar el siguiente piso hacia abajo
            print("Elevador descendiendo")
            next_stop = next((f for f in reversed(pending_floors) if f <= current_floor), None)
            if next_stop is not None:
                current_floor = next_stop
                pending_floors.remove(next_stop)
                print(f"Elevador se detiene -> {pending_floors}")
                pending_floors = actualizarPiso(current_floor, input_floors, pending_floors)
            else:
                direccion = "up"
                print("Elevador subiendo")

# Datos de entrada
mapaPisos = [5, 29, 13, 10]
pisosIngresados = {5: 2, 29: 10, 13: 1, 10: 1}
pisoInicial = ingresarPisoInicial()

# Ejecución del simulador
simularElevador(mapaPisos, pisoInicial, pisosIngresados)
