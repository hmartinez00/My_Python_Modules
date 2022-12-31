import os
import json
from Eliezer.speech_recognizer import Reconocimiento
from Eliezer.speech_recognizer import orders

# ruta_archivo_json = 'voice_comand_settings.json'

def recognizer(ruta_archivo_json):

    with open(ruta_archivo_json) as archivo_json:
        datos_json = json.load(archivo_json)

    close_options = datos_json['voice_optiones']['close']
    secuence_optionsA = datos_json['voice_optiones']['secuence'][0]
    secuence_optionsB = datos_json['voice_optiones']['secuence'][1]
    clear_options = datos_json['voice_optiones']['clear']


    file = 'temp/temp.txt'

    if os.path.isfile(file):
        pass
    else:
        os.mkdir('temp')
        string = ''
        with open(file, 'w', encoding='utf-8') as f:
            f.write(string)
        f.close()

    valor = False

    while valor == False:

        try:
            dictado = Reconocimiento()
            
            objeto = orders(file, dictado)
            
            if objeto.close_options(close_options):
                break        
            objeto.secuence_options(secuence_optionsA, secuence_optionsB)
            objeto.clear(clear_options)
        
        except:    
            continue