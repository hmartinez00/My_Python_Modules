import json


def setting_routes(
    key,
    prefix,
    sufix,
):
    file_routes = 'settings/routes/routes.json'

    with open(file_routes) as archivo_json:
        datos_json = json.load(archivo_json)
    ruta_archivo_json = []
    for i in datos_json[key]:
        ruta_archivo_json.append(prefix + i + sufix)
    
    return ruta_archivo_json