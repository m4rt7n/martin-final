# Trabajo final de programación: nosvolveremosaverleyton

## Autor: Martin Valderrama

Este proyecto implementa un algoritmo para resolver el juego clásico de sopa de letras. El programa permite al usuario buscar palabras específicas dentro de una sopa de letras utilizando un archivo de entrada que contiene tanto la matriz de letras como las palabras a buscar. Al final, el resultado se almacena en un archivo JSON indicando qué palabras fueron encontradas.

## Estructura del Proyecto
El proyecto está dividido en tres capas, cada una en un archivo separado:

1. **`input_layer.py`**: Contiene la función `get_file_content()` para leer el archivo de entrada y obtener la sopa de letras y las palabras a buscar.
2. **`logic_layer.py`**: Implementa la lógica de búsqueda de palabras con las funciones `find_word()` y `find_words()`.
3. **`output_layer.py`**: Utiliza las otras dos capas para generar un reporte en formato JSON que indica si cada palabra fue encontrada en la sopa de letras.

## Archivos
- `input_layer.py`: Función para leer el archivo de entrada.
- `logic_layer.py`: Funciones para encontrar palabras en la sopa de letras.
- `output_layer.py`: Coordina la ejecución y genera el reporte.
- `letter_soup.txt`: Archivo de entrada con la sopa de letras y las palabras a buscar.
- `soup_report.json`: Archivo de salida que contiene el reporte con las palabras encontradas y no encontradas.

## Formato del Archivo de Entrada
El archivo de entrada (`letter_soup.txt`) debe tener el siguiente formato:
1. **Matriz de letras**: Cada fila de la sopa de letras en mayúsculas, separadas por espacios.
2. **Separador**: Una línea con tres guiones (`---`) que indica el fin de la sopa de letras y el inicio de las palabras a buscar.
3. **Palabras a buscar**: Cada palabra en una línea separada. Las palabras pueden estar en mayúsculas o minúsculas.

### Ejemplo de `letter_soup.txt`
```
A M A R S
S T E R I
O M A Z C
A L C R H
P O L O S         <--
---               <-------no puede existir espacio entre la sopa de letras, el separador y las palabras
Amar              <--
Osa
atar
solo
polos
Mezclar
Palo
```

## Cómo Ejecutar el Código

### Prerrequisitos
- **Python 3**: Asegúrate de tener Python 3 instalado. Puedes verificar la instalación ejecutando:
  ```sh
  python --version
  ```

### Instrucciones de Ejecución
1. **Clonar el repositorio**: Clona este repositorio en tu máquina local.
   ```sh
   git clone https://github.com/m4rt7n/martin-final.git
   ```

2. **Navegar al directorio del proyecto**:
   - Abre una terminal y utiliza el comando `cd` para navegar al directorio donde se encuentra el repositorio clonado. Reemplaza `ruta/del/repositorio` con la ubicación correcta en tu máquina. Por ejemplo:
     ```sh
     cd ruta/del/repositorio
     ```

3. **Asegúrate de tener el archivo `letter_soup.txt`** en el mismo directorio que los scripts `input_layer.py`, `logic_layer.py` y `output_layer.py`.

4. **Ejecutar el script principal (`output_layer.py`)**:
   - Una vez en el directorio del proyecto, ejecuta el siguiente comando:
     ```sh
     python output_layer.py
     ```

5. **Resultado**: Una vez que el script se haya ejecutado, el reporte se generará en un archivo llamado `soup_report.json`. Verás un mensaje en la consola indicando la ruta donde se guardó el archivo de reporte.

### Ejemplo de Salida
El archivo `soup_report.json` tendrá un formato similar al siguiente:
```json
{
  "Amar": true,
  "Osa": true,
  "atar": true,
  "solo": true,
  "polos": true,
  "Mezclar": false,
  "Palo": false
}
```

## Notas Adicionales
- **Formato Consistente**: Asegúrate de que el archivo de entrada esté bien formateado (letras en mayúsculas, sin caracteres especiales, etc.) para evitar errores de ejecución.
- **Modificación de Archivo de Entrada**: Puedes modificar `letter_soup.txt` para probar diferentes sopas de letras y listas de palabras, teniendo en cuenta de que la sopa de letras debe estar formulada como una matriz, tal cual como en el ejemplo.

## Contacto
Si tienes preguntas o sugerencias, siéntete libre de abrir un **issue** o contactar al autor del proyecto.

¡Gracias por usar el Trabajo final de programación: nosvolveremosaverleyton!
