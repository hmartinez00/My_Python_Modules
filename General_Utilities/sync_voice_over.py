import os
import re


def find_files(directory, ext):
    f_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(ext):
                f_files.append(os.path.join(root, file))
    return f_files

def analizar_srt(original_srt):
    """
    Función para analizar un archivo de subtítulos SRT.

    Parámetros:
        original_srt (str): Ruta al archivo SRT.

    Salida:
        Imprime en la consola la longitud en caracteres de cada línea de subtítulo.
    """

    # Expresión regular para las marcas de tiempo
    regex_marca_tiempo = r"^\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+$"

    with open(original_srt, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    
    mark_index = [False for _ in range(len(lineas))]

    # Bucle para iterar por las líneas
    for i, linea in enumerate(lineas):
        # Si la línea actual es una marca de tiempo
        if re.match(regex_marca_tiempo, linea):
            # Obtener la siguiente línea (asumiendo que es el subtítulo)
            subtitulo = lineas[i + 1]
            # Eliminar saltos de línea
            subtitulo = subtitulo.strip()
            # calcular el numero de caracteres
            longitud = len(subtitulo) + 1
            # Tomando el indice de marca temporal
            mark_index[i] = lineas[i].replace('\n', '') + f" [{longitud}]" + '\n'
            # Modificar la línea de marca de tiempo
            lineas[i] = mark_index[i]

    # Escribir las líneas modificadas al archivo
    with open(original_srt, "w", encoding="utf-8") as f:
        f.writelines(lineas)