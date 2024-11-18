# Archivo: output_layer.py
import json

def generate_report(letter_soup, words, output_file="reporte_sopa_letras.json"):
    """
    Genera un reporte en formato JSON con las palabras encontradas y no encontradas en la sopa de letras.
    
    :param letter_soup: Matriz de letras.
    :param words: Lista de palabras a buscar.
    :param output_file: Nombre del archivo JSON de salida.
    """
    from logic_layer import find_words  # Importar la función find_words desde la capa lógica
    
    # Encontrar las palabras en la sopa de letras utilizando la función find_words
    report = find_words(letter_soup, words)
    
    # Abrir el archivo de salida y escribir el reporte en formato JSON
    with open(output_file, 'w') as json_file:
        json.dump(report, json_file, indent=4)  # Guardar el reporte en formato JSON con una indentación de 4 espacios
    
    # Imprimir la ubicación del archivo generado
    print(f"El reporte ha sido almacenado en: {output_file}")

# Ejemplo de uso
if __name__ == "__main__":
    from input_layer import get_file_content  # Importar la función get_file_content desde la capa de entrada
    
    # Definir la ruta del archivo de entrada (modificar según la ubicación del archivo)
    file_path = "sopa_letras.txt"  # Cambiar por la ruta del archivo de entrada
    
    # Obtener la sopa de letras y las palabras a buscar desde el archivo de entrada
    letter_soup, words = get_file_content(file_path)
    
    # Generar el reporte en formato JSON
    generate_report(letter_soup, words)
