import time

def ingresarPisoInicial():
     time.sleep(1)
     pisoInicial = int(input("\nPiso inicial de ejecucion: "))
     return pisoInicial

def simularElevador(pisos, piso_inicial, mapa_pisos):
    """
    Simula el funcionamiento de un elevador en un edificio de 29 pisos.
    
    :param pisos: Lista de pisos a los cuales se llama el elevador en orden definido.
    :param piso_inicial: Piso inicial del elevador.
    :param mapa_pisos: Diccionario donde las claves son los pisos de llamada y los valores son los destinos.
    """
    piso_actual = piso_inicial
    direccion = "subiendo" if pisos[0] > piso_inicial else "bajando"
    historial = []
    
    def imprimir_estado(mensaje):
        print(mensaje)
        historial.append(mensaje)
    
    imprimir_estado(f"Arreglo de pisos: {pisos}")
    imprimir_estado(f"Piso inicial de ejecución: {piso_inicial}")
    imprimir_estado(f"Pisos ingresados: {mapa_pisos}")
    imprimir_estado(f"Sentido inicial: {direccion}")

    while pisos:
        # Ordenar los pisos según la dirección actual
        if direccion == "subiendo":
            pisos.sort()
        else:
            pisos.sort(reverse=True)
        
        # Determinar el siguiente piso y moverse hacia él
        siguiente_piso = pisos[0]
        imprimir_estado(f"Elevador en piso {piso_actual}")
        imprimir_estado(f"Elevador {'subiendo' if siguiente_piso > piso_actual else 'bajando'}")
        
        for piso in range(piso_actual, siguiente_piso, 1 if siguiente_piso > piso_actual else -1):
            imprimir_estado(f"Elevador en piso {piso + (1 if siguiente_piso > piso_actual else -1)}")
        
        piso_actual = siguiente_piso
        
        # Detenerse en el piso actual
        imprimir_estado(f"Elevador se detiene → {pisos}")
        pisos.pop(0)  # Eliminar el piso alcanzado de las solicitudes
        #imprimir_estado(f"Elevador se detiene → {pisos}")
        
        # Si el piso actual está en mapa_pisos, agregar el destino
        if piso_actual in mapa_pisos:
            nuevo_piso = mapa_pisos[piso_actual]
            pisos.append(nuevo_piso)
            imprimir_estado(f"Piso ingresado {nuevo_piso} → {pisos}")
        
        # Cambiar dirección si es necesario
        if not any(p > piso_actual for p in pisos) and direccion == "subiendo":
            direccion = "bajando"
            imprimir_estado("Elevador cambia dirección a bajando")
        elif not any(p < piso_actual for p in pisos) and direccion == "bajando":
            direccion = "subiendo"
            imprimir_estado("Elevador cambia dirección a subiendo")
    
    imprimir_estado("Elevador finaliza su recorrido")
    return historial





# Ejemplo de uso
if __name__ == "__main__":
    arreglo_pisos = [5, 29, 13, 10]
    piso_inicial = ingresarPisoInicial()
    mapa_pisos = {5: 2, 
                  29: 10, 
                  13: 1, 
                  10: 1}
    
    historial = simularElevador(arreglo_pisos, piso_inicial, mapa_pisos)





















