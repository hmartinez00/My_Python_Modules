import json
from General_Utilities.cntrl_exit import salida
from Pku_module.Package_update_module import listar_paquetes, actualizar_setup, actualizar_paquetes


dir_dist = 'dist'

ruta_archivo_json = 'Package_update/settings_setups.json'
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

projects = listar_paquetes()

for project in projects:
    package = datos_json[project]
    actualizar_setup(package)
    actualizar_paquetes(dir_dist, project)

salida("Package_update/builder")