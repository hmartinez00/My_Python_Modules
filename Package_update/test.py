import os
import json
from Pku_module.Package_update_module import listar_paquetes

# print(listar_paquetes())

version = input('Introduzca la nueva version: ')

ruta_archivo_json = 'Package_update/settings_setups.json'
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

datos_json['Pku_module']['version'] = version

with open(ruta_archivo_json, 'w') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)