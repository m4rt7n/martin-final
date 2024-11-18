import json

def find_word(letter_soup, word):
    # Dimensiones de la sopa de letras
    rows = len(letter_soup)
    cols = len(letter_soup[0]) if rows > 0 else 0
    
    # Convertir la palabra a mayúsculas para que coincida con la sopa de letras
    word = word.upper()
    
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
    found_words = {}
    for word in words:
        found_words[word] = find_word(letter_soup, word)
    return found_words

def generate_report(letter_soup, words):
    report = find_words(letter_soup, words)
    return report

def get_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    # Separar la sopa de letras y las palabras a buscar
    letter_soup = []
    words = []
    parsing_soup = True
    for line in content:
        stripped_line = line.strip()
        if stripped_line == "---":
            parsing_soup = False
            continue
        if parsing_soup:
            if all(c.isalpha() or c.isspace() for c in stripped_line):
                letter_soup.append(list(stripped_line.replace(" ", "").upper()))
        else:
            if stripped_line.isalpha():
                words.append(stripped_line)
    return letter_soup, words

def main(file_path):
    # Obtener el contenido del archivo
    letter_soup, words = get_file_content(file_path)
    
    # Generar el reporte
    report = generate_report(letter_soup, words)
    
    # Guardar el reporte en un archivo JSON
    output_file = "reporte_sopa_letras.json"
    with open(output_file, 'w') as json_file:
        json.dump(report, json_file, indent=4)
    
    # Imprimir la ruta del archivo generado
    print(f"El reporte ha sido almacenado en: {output_file}")

# Ejemplo de uso
if __name__ == "__main__":
    file_path = "sopa_letras.txt"  # Cambiar por la ruta del archivo de entrada
    main(file_path)
