import json


def setting_routes(
    key,
    prefix: str = None,
    sufix: str = None,
):
    file_routes = 'settings/routes/routes.json'

    with open(file_routes) as archivo_json:
        datos_json = json.load(archivo_json)
    ruta_archivo = []
    
    prefix = 'settings/' + key + '/' if prefix is None else prefix

    for i in datos_json[key]:
        ruta_archivo.append([i, prefix + i + sufix])
    
    return ruta_archivo