import time

def ingresarPisoInicial():
     time.sleep(1)
     pisoInicial = int(input("\nPiso inicial de ejecucion: "))
     return pisoInicial

def simularElevador(pisos, piso_inicial, mapa_pisos):

    piso_actual = piso_inicial
    direccion = "subiendo" if pisos[0] > piso_inicial else "bajando"
    historial = []
    
    def imprimir_estado(mensaje):
        print(mensaje)
        historial.append(mensaje)
    
    imprimir_estado(f"Arreglo de pisos: {pisos}")
    imprimir_estado(f"Piso inicial de ejecución: {piso_inicial}")
    imprimir_estado(f"Pisos ingresados: {mapa_pisos}")
    imprimir_estado(f"Sentido inicial: {direccion}\n")

    while pisos:
        # Tomar el siguiente piso en orden
        siguiente_piso = pisos.pop(0)

        imprimir_estado(f"Elevador en piso {piso_actual}")
        imprimir_estado(f"Elevador {'subiendo' if siguiente_piso > piso_actual else 'bajando'}")
        
        # Moverse hasta el siguiente piso
        while piso_actual != siguiente_piso:
            piso_actual += 1 if siguiente_piso > piso_actual else -1
            imprimir_estado(f"Elevador en piso {piso_actual}")
        
        # Detenerse en el piso actual
        imprimir_estado(f"Elevador se detiene -> {pisos}")
        
        # Si el piso actual está en mapa_pisos, agregar el destino al final de la cola
        if piso_actual in mapa_pisos:
            nuevo_piso = mapa_pisos[piso_actual]
            pisos.append(nuevo_piso)  # Añadir el destino al final de la cola
            imprimir_estado(f"Piso ingresado {nuevo_piso} -> {pisos}")
        
        # Determinar si se debe cambiar la dirección (opcional)
        if pisos:
            direccion = "subiendo" if pisos[0] > piso_actual else "bajando"
            imprimir_estado(f"Elevador cambia dirección a {direccion}")

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


"""
Documentación
Funciones Principales
ingresarPisoInicial:

Solicita al usuario el piso inicial desde el cual debe comenzar el elevador.
Devuelve el valor como un número entero.
simularElevador:

Controla la lógica del recorrido del elevador.
Imprime los estados del elevador, como el piso actual, dirección, paradas y cambios en la cola de pisos.
Administra las solicitudes de destinos mediante el diccionario mapa_pisos.
imprimir_estado:

Función auxiliar para imprimir mensajes y almacenarlos en un historial para posibles análisis o depuración.
Variables y Parámetros
arreglo_pisos: Lista de pisos a los cuales el elevador debe ir en el orden en que se llaman.
piso_inicial: Piso desde donde comienza el elevador.
mapa_pisos: Diccionario que mapea pisos de llamada a destinos ingresados.

"""
