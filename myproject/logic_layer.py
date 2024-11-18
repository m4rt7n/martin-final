# Archivo: logic_layer.py

def find_word(letter_soup, word):
    """
    Busca una palabra en la sopa de letras.
    
    :param letter_soup: Matriz de letras.
    :param word: Palabra a buscar.
    :return: True si la palabra se encuentra, False de lo contrario.
    """
    rows = len(letter_soup)
    cols = len(letter_soup[0]) if rows > 0 else 0
    word = word.upper()  # Convertir la palabra a mayúsculas para evitar problemas de coincidencia

    # Definir todas las posibles direcciones de movimiento (8 direcciones)
    directions = [
        (0, 1),  # derecha
        (1, 0),  # abajo
        (0, -1), # izquierda
        (-1, 0), # arriba
        (1, 1),  # diagonal abajo-derecha
        (-1, -1),# diagonal arriba-izquierda
        (1, -1), # diagonal abajo-izquierda
        (-1, 1)  # diagonal arriba-derecha
    ]

    # Función para verificar si una palabra existe comenzando desde una posición dada
    def check_word(x, y, word, direction):
        dx, dy = direction
        for i in range(len(word)):
            new_x, new_y = x + i * dx, y + i * dy
            # Verificar si está fuera de los límites o si no coincide la letra
            if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols or letter_soup[new_x][new_y] != word[i]:
                return False
        return True

    # Buscar la palabra en toda la sopa de letras
    for i in range(rows):
        for j in range(cols):
            # Si encontramos la primera letra, comenzamos a verificar en todas las direcciones
            if letter_soup[i][j] == word[0]:
                for direction in directions:
                    if check_word(i, j, word, direction):
                        return True
    return False

def find_words(letter_soup, words):
    """
    Busca una lista de palabras en la sopa de letras.
    
    :param letter_soup: Matriz de letras.
    :param words: Lista de palabras a buscar.
    :return: Diccionario con cada palabra como clave y un valor booleano indicando si fue encontrada o no.
    """
    found_words = {}
    for word in words:
        found_words[word] = find_word(letter_soup, word)  # Llamar a find_word para cada palabra
    return found_words
