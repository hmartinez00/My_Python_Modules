import json
from General_Utilities.cntrl_exit import salida


ruta_archivo_json = 'settings_setups.json'
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

project = input('Introduzca el nombre del proyecto: ')

try:
    package = datos_json[project]

    string = f'''from setuptools import setup

setup(
    name='{package['name']}',
    version='{package['version']}',
    description='{package['description']}',
    author='{package['author']}',
    author_email='{package['author_email']}',
    url='{package['url']}',
    packages={package['packages']}
)'''

    file = 'setup.py'
    f = open(file, 'w')
    f.write(string)
    f.close()

except:
    print('Proyecto no encontrado!')

salida("setup_generator")