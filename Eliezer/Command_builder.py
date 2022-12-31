import json

ruta_archivo_json = 'voice_comand_settings.json'

datos_json = \
{
    "voice_optiones":{
        "close":[
            "finalizar dictado",
            "finalizar comunicación",
            "cerrar comunicación",
            "cierra comunicación"
        ],
        "secuence":[
            ["nueva línea", "\n"],
            ["nuevo párrafo", "\n\n"]
        ],
        "clear":[
            "borrar todo"
        ]
    }
}

with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)