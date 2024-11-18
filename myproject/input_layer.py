# Archivo: input_layer.py

def get_file_content(file_path):
    """
    Lee el archivo de entrada y devuelve la sopa de letras y las palabras a buscar.
    
    :param file_path: Ruta del archivo de entrada.
    :return: Una tupla (letter_soup, words) donde letter_soup es la matriz de letras y words es la lista de palabras a buscar.
    """
    with open(file_path, 'r') as file:
        content = file.readlines()  # Leer todas las líneas del archivo
    
    # Separar la sopa de letras y las palabras a buscar
    letter_soup = []
    words = []
    parsing_soup = True  # Variable para saber si estamos leyendo la sopa de letras o las palabras

    for line in content:
        stripped_line = line.strip()  # Remover espacios al inicio y al final de la línea

        # Si encontramos el separador "---", cambiamos al modo de lectura de palabras
        if stripped_line == "---":
            parsing_soup = False
            continue

        if parsing_soup:
            # Si estamos en la parte de la sopa de letras, agregamos la línea a la matriz de letras
            if all(c.isalpha() or c.isspace() for c in stripped_line):
                letter_soup.append(list(stripped_line.replace(" ", "").upper()))  # Convertir a mayúsculas y eliminar espacios
        else:
            # Si estamos en la parte de las palabras a buscar, agregamos cada palabra a la lista de palabras
            if stripped_line.isalpha():
                words.append(stripped_line)

    return letter_soup, words  # Retornar la sopa de letras y las palabras a buscar
