import json
from General_Utilities.cntrl_exit import salida
from General_Utilities.option_list import option_list
from Pku_module.Package_update_module import project_route, listar_paquetes, actualizar_paquetes

ruta_archivo_json = 'Package_update/settings_setups.json'
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

opciones=listar_paquetes()
project = option_list(opciones)

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

salida("Package_update/setup_generator")