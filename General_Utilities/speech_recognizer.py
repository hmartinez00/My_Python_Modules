# pip intall speechrecognition
# Puede requerir previamente:
# 
# pip install pipwin
# pipwin install pyaudio

import speech_recognition as sr

def Reconocimiento():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Te escucho: ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="es-ES")
    except:
        print('No te he entendido')

    return text

class orders:

    def __init__(
        self,
        file,
        __dictado__
    ):

        f = open(file, 'r')
        string = f.read()
        f.close()

        self.file = file
        self.string = string
        self.__dictado__ = __dictado__

    def close_options(self):
        if \
            'finalizar dictado' in self.__dictado__ or \
            'finalizar comunicación' in self.__dictado__ or \
            'cerrar comunicación' in self.__dictado__ or \
            'cierra comunicación' in self.__dictado__:
            
            return True

    def continue_options(self):
        if 'nueva línea' in self.__dictado__:
            string = string + '\n'
            return string

        elif 'nuevo párrafo' in self.__dictado__:
            string = string + '\n\n'
            return string

    def clear(self):
        if 'borrar todo' in self.__dictado__:
            string = ''
            f = open(self.file, 'w')
            f.write(string)
            f.close()
        else:
            string = string + ' ' + str(self.__dictado__)
