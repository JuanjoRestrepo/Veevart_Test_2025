
def showGrid(grid):
    print("\n==== GRID ====")
    for i in grid:
        print(i)


def findInGrid(grid, words):
    def searchWord(word):
        rows = len(matrix)
        cols = len(matrix[0])

        # Buscar horizontalmente (de izquierda a derecha)
        for r in range(rows):
            for c in range(cols - len(word) + 1):
                if "".join(matrix[r][c:c + len(word)]) == word:
                    return [(char, [r, c + i]) for i, char in enumerate(word)]

        # Buscar verticalmente (de arriba a abajo)
        for c in range(cols):
            for r in range(rows - len(word) + 1):
                if "".join(matrix[r + i][c] for i in range(len(word))) == word:
                    return [(char, [r + i, c]) for i, char in enumerate(word)]

        return None

    # Convertir la matriz de texto a una lista de listas
    matrix = [row.split() for row in grid]

    # Buscar cada palabra
    for word in words:
        print(f"\nSearching \"{word}\"")
        result = searchWord(word)
        if result:
            for char, pos in result:
                print(f"{char} - {pos}")
        else:
            print(f"\"{word}\" Not found")

# Test de prueba
grid = ["S O L", "U N O", "N U T"]
words = ["SUN", "SOL", "LOT", "ONU", "RAY", "MOM"]


if __name__ == "__main__":
    showGrid(grid)
    findInGrid(grid, words)

"""
Documentación de las Funciones
1. showGrid(grid):
Función para imprimir la cuadrícula de manera visual.
Cada fila de la cuadrícula se imprime línea por línea, facilitando su lectura.

2. findInGrid(grid, words):
Busca palabras en la cuadrícula considerando únicamente direcciones horizontales (de izquierda a derecha) y verticales (de arriba a abajo).
Se apoya en la función interna searchWord, que realiza la búsqueda palabra por palabra.
Convierte la cuadrícula en una lista de listas para facilitar el acceso a los elementos.

3. searchWord(word):
Revisa todas las filas y columnas buscando coincidencias exactas con la palabra dada.
Devuelve una lista con las posiciones de cada carácter si encuentra la palabra, o None si no la encuentra.

"""
