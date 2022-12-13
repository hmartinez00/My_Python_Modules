import json
import os

# Actualizando Json

package_name = input('Introduzca el nombre del nuevo paquete: ')
package_description = input('Introduzca la desripcion del nuevo paquete: ')

param = {}
param["name"] = package_name
param["version"] = "0.1"
param["description"] = package_description
param["author"] = "Hector Martinez"
param["author_email"] = "hectoralonzomartinez00@gmail.com"
param["url"] = ''
param["packages"] = [
    package_name,
]

ruta_archivo_json = 'Package_update/settings_setups.json'
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

datos_json[package_name] = param

with open(ruta_archivo_json, 'w') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)


# Creando directorio del paquete

os.makedirs(package_name)
file = package_name + '/__init__.py'
f = open(file, 'w')
f.write("")
f.close()