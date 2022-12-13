import json
from General_Utilities.cntrl_exit import salida
from General_Utilities.option_list import option_list
from Pku_module.Package_update_module import project_route, listar_paquetes, actualizar_setup,actualizar_paquetes


opciones = listar_paquetes()

ruta_archivo_json = 'Package_update/settings_setups.json'
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

project = option_list(opciones)
package = datos_json[project]

actualizar_setup(package)

salida("Package_update/setup_generator")