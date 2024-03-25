import os
import time
import json
from Eliezer.speech_recognizer import orders
from Eliezer.speech_recognizer import Reconocimiento


def recognizer(ruta_archivo_json, file):

    with open(ruta_archivo_json) as archivo_json:
        datos_json = json.load(archivo_json)

    close_options       = datos_json['voice_options']['close']
    secuence_optionsA   = datos_json['voice_options']['secuence'][0]
    secuence_optionsB   = datos_json['voice_options']['secuence'][1]
    clear_options       = datos_json['voice_options']['clear']
    valor               = datos_json['close'][0]

    while valor == 1:
        try:            
            dictado = Reconocimiento()
            
            objeto = orders(file, dictado)
            
            if objeto.close_options(close_options):
                break        
            objeto.secuence_options(secuence_optionsA, secuence_optionsB)
            objeto.clear(clear_options)

            time.sleep(1)

            with open(ruta_archivo_json) as archivo_json:
                datos_json = json.load(archivo_json)
            
            valor = datos_json['close'][0]
        
        except:    
            continue   

    datos_json['close'][0] = 1
    with open(ruta_archivo_json, 'w') as f:
        json.dump(datos_json, f, indent=4)  # Añadir indentación para legibilidad
