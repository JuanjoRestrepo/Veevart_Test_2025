# Veevart_Test_2025


# Documentación por secciones

# 1. Elevador
## Funciones Principales
## ingresarPisoInicial:
Solicita al usuario el piso inicial desde el cual debe comenzar el elevador. Devuelve el valor como un número entero.

## simularElevador:
Controla la lógica del recorrido del elevador.
Imprime los estados del elevador, como el piso actual, dirección, paradas y cambios en la cola de pisos.
Administra las solicitudes de destinos mediante el diccionario mapa_pisos.

## imprimir_estado:
Función auxiliar para imprimir mensajes y almacenarlos en un historial para posibles análisis o depuración.
Variables y Parámetros
- arreglo_pisos: Lista de pisos a los cuales el elevador debe ir en el orden en que se llaman.
- piso_inicial: Piso desde donde comienza el elevador.
- mapa_pisos: Diccionario que mapea pisos de llamada a destinos ingresados.


# 2. Sopa de letras
## showGrid(grid):
Función para imprimir visualmente la cuadrícula, línea por línea.
Útil para verificar cómo está estructurada la cuadrícula antes de realizar la búsqueda.

## findInGrid(grid, words):
Realiza la búsqueda de cada palabra en la lista words.
Convierte la cuadrícula (lista de cadenas) en una matriz bidimensional para facilitar el acceso a los caracteres.
Usa la función interna searchWord para buscar palabras de forma horizontal y vertical.

## searchWord(matrix, word):
Busca una palabra en la matriz en dos direcciones:
Horizontal: De izquierda a derecha dentro de las filas.
Vertical: De arriba a abajo dentro de las columnas.
Si encuentra la palabra, devuelve una lista de mapas que contiene:
- El carácter encontrado.
- Las coordenadas de cada carácter en la matriz ([fila, columna]).
- Si no encuentra la palabra, devuelve null.

## Cómo usar el código
- Crea un List<String> para representar la cuadrícula.
- Crea un List<String> con las palabras que deseas buscar.
- Llama a las funciones showGrid y findInGrid para realizar la búsqueda.
- En Apex, abrir la consola de *Execute Anonymous Windows* en la sección de *Debug* e introducir la línea: *SopaDeLetras.test();*
- Darle check a *OpenLog*, luego en *Execute*, luego hacer check en *Debug Only* para visualizar las salidas de la ejecución.


### Mostrar la cuadrícula
1. WordSearch.showGrid(grid);
### Buscar palabras
1. WordSearch.findInGrid(grid, words);
Output esperado en la consola de depuración
Muestra la cuadrícula inicial.
Detalla cada paso en la búsqueda, incluyendo las posiciones evaluadas y si encuentra o no las palabras.
