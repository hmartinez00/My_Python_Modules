import os
import json
import subprocess
from General_Utilities.option_list import list_files


def project_requirements():

    # -------------------------------------
    # Creando el archivo de requerimientos
    # si no existe.
    # -------------------------------------
    directorio = 'settings/requirements'
    ruta_archivo_json = f'{directorio}/requirements.json'
    installed_packages = f'{directorio}/installed_packages.txt'
    requirements = 'requirements.txt'
    datos_json = {}
    librerias = []
    datos_json['Librerias'] = librerias

    if \
        os.path.isfile(ruta_archivo_json) and \
        os.path.isfile(installed_packages):
        pass
    else:
        if os.path.isdir(directorio):
            pass
        else:
            os.makedirs(directorio)

        subprocess.run(f'pip freeze >> {installed_packages}', shell=True)

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
                if 'from' in line and '.' in line:
                    element_paquetes = line.split('\n')[0].split(' ')[1].split('.')[0]
                    element_modulos = line.split('\n')[0].split(' ')[1].split('.')[1]
                    element_clases_funciones = line.split('\n')[0].split(' ')[-1]
                    print(file, datos_json.keys())
                    if element_paquetes not in datos_json.keys():
                        datos_json[element_paquetes] = [element_modulos]
                    elif element_paquetes in datos_json.keys():
                        lista_modulos = datos_json[element_paquetes]
                        if element_modulos not in lista_modulos:
                            lista_modulos.append(element_modulos)
                        datos_json[element_paquetes] = lista_modulos

                if 'import ' in line and 'from' not in line:
                    element_paquetes = line.split('\n')[0].split(' ')[1]
                    print(datos_json.keys())
                    if element_paquetes not in librerias:
                        librerias.append(element_paquetes)
                
                datos_json['Librerias'] = librerias

    # -------------------------------------
    # Extrayendo listas a cotejar
    # -------------------------------------
    keys = list(datos_json.keys())
    packages = []
    with open(installed_packages, encoding='utf-8') as f:
        for line in f:
            packages.append(line)

    # print(keys, packages)

    # -------------------------------------
    # Creando el archivo requirements
    # -------------------------------------
    string = ''
    with open(requirements, 'w', encoding='utf-8') as f:
        f.write(string)
    f.close()

    string = ''
    for i in keys:
        for j in packages:
            if i.replace('_', '-') in j:
                string = string + j

    with open(requirements, 'w', encoding='utf-8') as f:
        f.write(string)
    f.close()

    # -------------------------------------
    # Volcando la informacion al json
    # -------------------------------------
    with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
        json.dump(datos_json, archivo_json, indent=4)
    os.remove(installed_packages)
