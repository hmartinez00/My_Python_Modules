import os
import json
from General_Utilities.option_list import list_files


def project_requirements():

    # -------------------------------------
    # Creando el archivo de requerimientos
    # si no existe.
    # -------------------------------------
    ruta_archivo_json = 'settings/requirements/requirements.json'
    datos_json = {}
    librerias = []
    datos_json['librerias'] = librerias

    if os.path.isfile(ruta_archivo_json):
        pass
    else:
        os.makedirs('settings/requirements')
        with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
            json.dump(datos_json, archivo_json, indent=4)

    # -------------------------------------
    # Determinando modulos y paquetes del
    # proyecto.
    # -------------------------------------
    lista = list_files('.')
    py_files = [i for i in lista if '.py' in i and '.pyc' not in i and 'Project_requirements.py' not in i]

    for file in py_files:
        print(file)
        with open(file, encoding='utf-8') as f:
            for line in f:
                if 'import ' in line and 'from' in line:
                    element_paquetes = line.split('\n')[0].split(' ')[1]
                    element_modulos = line.split('\n')[0].split(' ')[-1]
                    print(datos_json.keys())
                    if element_paquetes not in datos_json.keys():
                        datos_json[element_paquetes] = [element_modulos]
                    elif element_paquetes not in datos_json.keys():
                        datos_json[element_paquetes].append(element_modulos)

                if 'import ' in line and 'from' not in line:
                    element_paquetes = line.split('\n')[0].split(' ')[1]
                    print(datos_json.keys())
                    if element_paquetes not in librerias:
                        librerias.append(element_paquetes)
                
                datos_json['librerias'] = librerias

    # -------------------------------------
    # Volcando la informacion al json
    # -------------------------------------
    with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
        json.dump(datos_json, archivo_json, indent=4)