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
            [
                "nueva línea", 
                "nuevo párrafo",
                "signo de coma",
                "signo de punto",
                "signo de punto y aparte",
                "signo de punto y coma",
                "signo de dos puntos",
                "abrir signo de interrogación",
                "cerrar signo de interrogación",
                "abrir signo de exclamación",
                "cerrar signo de exclamación",
                "abrir paréntesis",
                "cerrar paréntesis",
            ],
            [
                "\n",
                "\n\n",
                ",",
                ".",
                ".\n\n",
                ";",
                ":",
                "¿",
                "?",
                "¡",
                "!",
                "(",
                ")",
            ]
        ],
        "clear":[
            "borrar todo"
        ]
    }
}

with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)