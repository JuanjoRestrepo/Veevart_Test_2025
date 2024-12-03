public class SopaDeLetras {

    public static void showGrid(List<String> grid) {
        System.debug('==== GRID ====');
        for (String row : grid) {
            System.debug(row);
        }
    }

    public static void findInGrid(List<String> grid, List<String> words) {
        List<List<String>> matrix = new List<List<String>>();

        // Convertir el grid en una matriz
        for (String row : grid) {
            matrix.add(row.split(' '));
        }


        // Buscar cada palabra
        for (String word : words) {
            System.debug('\nSearching "' + word + '"');
            
            //Llamamos a la función search
            List<Map<String, Object>> result = searchWord(matrix, word);

            if (result != null) {
                for (Map<String, Object> entry : result) {
                    System.debug(entry.get('char') + ' - ' + entry.get('pos'));
                }
            } else {
                System.debug('"' + word + '" Not found');
            }
        }
    }

    public static List<Map<String, Object>> searchWord(List<List<String>> matrix, String word) {
        Integer rows = matrix.size();
        Integer cols = matrix[0].size();
        List<Map<String, Object>> foundPositions = new List<Map<String, Object>>();

        // Buscar horizontalmente (de izquierda a derecha)
        for (Integer r = 0; r < rows; r++) {
            for (Integer c = 0; c <= cols - word.length(); c++) {
                String horizontalSlice = '';
                for (Integer i = 0; i < word.length(); i++) {
                    horizontalSlice += matrix[r][c + i];
                }

                //System.debug('Horizontal Check at Row ' + r + ', Col ' + c + ': ' + horizontalSlice);
                if (horizontalSlice == word) {
                    for (Integer i = 0; i < word.length(); i++) {
                        Map<String, Object> pos = new Map<String, Object>{
                            'char' => String.fromCharArray(new List<Integer>{word.charAt(i)}),
                            'pos' => new List<Integer>{r, c + i}
                        };
                        foundPositions.add(pos);
                    }
                    return foundPositions;
                }
            }
        }

        // Buscar verticalmente (de arriba a abajo)
        for (Integer c = 0; c < cols; c++) {
            for (Integer r = 0; r <= rows - word.length(); r++) {
                String verticalSlice = '';
                for (Integer i = 0; i < word.length(); i++) {
                    verticalSlice += matrix[r + i][c];
                }

                
                if (verticalSlice == word) {
                    for (Integer i = 0; i < word.length(); i++) {
                        Map<String, Object> pos = new Map<String, Object>{
                            'char' => String.fromCharArray(new List<Integer>{word.charAt(i)}),
                            'pos' => new List<Integer>{r + i, c}
                        };
                        foundPositions.add(pos);
                    }
                    return foundPositions;
                }
            }
        }

        // Si no se encuentra, devolver null
        return null;
    }

	// Test de prueba
    public static void test() {
        List<String> grid = new List<String>{'S O L', 'U N O', 'N U T'};
        List<String> words = new List<String>{'SUN', 'SOL', 'LOT', 'ONU', 'RAY', 'MOM'};

        showGrid(grid);
        findInGrid(grid, words);
    }

}
