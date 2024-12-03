def find_words_in_grid(grid, words):
    def search_word(word):
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

    # Procesar cada palabra
    for word in words:
        print(f"Searching \"{word}\"")
        result = search_word(word)
        if result:
            for char, pos in result:
                print(f"{char} - {pos}")
        else:
            print(f"\"{word}\" Not found")


# Ejemplo de uso
grid = ["S O L", "U N O", "N U T"]
words = ["SUN", "SOL", "LOT", "ONU", "RAY"]

find_words_in_grid(grid, words)