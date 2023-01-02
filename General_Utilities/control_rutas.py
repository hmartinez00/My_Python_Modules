import json


def setting_routes(key):
    file_routes = 'settings/routes/routes.json'

    with open(file_routes) as archivo_json:
        datos_json = json.load(archivo_json)
    ruta_archivo = []
    for i in datos_json[key]:
        ruta_archivo.append(i)
    
    return ruta_archivo