# Sopa de Letras Solver

Este proyecto implementa un algoritmo para resolver el juego clásico de sopa de letras. El programa permite al usuario buscar palabras específicas dentro de una sopa de letras utilizando un archivo de entrada que contiene tanto la matriz de letras como las palabras a buscar. Al final, el resultado se almacena en un archivo JSON indicando qué palabras fueron encontradas.

## Características
- **Búsqueda de Palabras**: Busca palabras en todas las direcciones posibles (horizontal, vertical, y diagonal).
- **Reporte JSON**: Genera un archivo JSON con un reporte que indica si cada palabra fue encontrada en la sopa de letras.
- **Interfaz de Archivo de Entrada**: Utiliza un archivo `.txt` que contiene la sopa de letras y las palabras a buscar.

## Archivos
- `sopa_letras_solver.py`: Script principal que contiene todo el código para resolver la sopa de letras.
- `sopa_letras.txt`: Archivo de entrada con la sopa de letras y las palabras a buscar.
- `reporte_sopa_letras.json`: Archivo de salida que contiene el reporte con las palabras encontradas y no encontradas.

## Formato del Archivo de Entrada
El archivo de entrada (`sopa_letras.txt`) debe tener el siguiente formato:
1. **Matriz de letras**: Cada fila de la sopa de letras en mayúsculas, separadas por espacios.
2. **Separador**: Una línea con tres guiones (`---`) que indica el fin de la sopa de letras y el inicio de las palabras a buscar.
3. **Palabras a buscar**: Cada palabra en una línea separada. Las palabras pueden estar en mayúsculas o minúsculas.

### Ejemplo de `sopa_letras.txt`
```
A M A R S
S T E R I
O M A Z C
A L C R H
P O L O S
---
Amar
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
   git clone https://github.com/tu_usuario/sopa_letras_solver.git
   ```

2. **Navegar al directorio**: Cambia al directorio del proyecto.
   ```sh
   cd sopa_letras_solver
   ```

3. **Preparar el archivo de entrada**: Asegúrate de tener el archivo `sopa_letras.txt` en el mismo directorio que el script `sopa_letras_solver.py`. El archivo debe seguir el formato especificado anteriormente.

4. **Ejecutar el script**: Ejecuta el script utilizando Python.
   ```sh
   python sopa_letras_solver.py
   ```

5. **Resultado**: Una vez que el script se haya ejecutado, el reporte se generará en un archivo llamado `reporte_sopa_letras.json`. Verás un mensaje en la consola indicando la ruta donde se guardó el archivo de reporte.

### Ejemplo de Salida
El archivo `reporte_sopa_letras.json` tendrá un formato similar al siguiente:
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
- **Modificación de Archivo de Entrada**: Puedes modificar `sopa_letras.txt` para probar diferentes sopas de letras y listas de palabras.

## Contacto
Si tienes preguntas o sugerencias, siéntete libre de abrir un **issue** o contactar al mantenedor del proyecto.

¡Gracias por usar Sopa de Letras Solver!

