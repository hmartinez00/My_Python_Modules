import json


param = {}
param["name"] = ''
param["version"] = ''
param["description"] = ''
param["author"] = ''
param["author_email"] = ''
param["url"] = ''
param["packages"] = ''


ruta_archivo_json = 'Package_update/settings_setups.json'
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)


datos_json['nueva'] = param
# datos_json['nueva']["name"] = ''
# datos_json['nueva']["version"] = ''
# datos_json['nueva']["description"] = ''
# datos_json['nueva']["author"] = ''
# datos_json['nueva']["author_email"] = ''
# datos_json['nueva']["url"] = ''
# datos_json['nueva']["packages"] = ''

with open(ruta_archivo_json, 'w') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)