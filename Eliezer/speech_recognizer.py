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


        self.file = file
        self.__dictado__ = __dictado__

        string = ''
        with open(self.file, encoding='utf-8') as f:
            for line in f:
                string = string + line
        
        self.string = string

    def close_options(self):
        if \
            'finalizar dictado' in self.__dictado__ or \
            'finalizar comunicación' in self.__dictado__ or \
            'cerrar comunicación' in self.__dictado__ or \
            'cierra comunicación' in self.__dictado__:
           
            return True

    def continue_options(self):

        if 'nueva línea' in self.__dictado__:
            string = self.string + '\n'

        elif 'nuevo párrafo' in self.__dictado__:
            string = self.string + '\n\n'
        
        else:
            string = self.string + ' ' + str(self.__dictado__)
        
        with open(self.file, 'w', encoding='utf-8') as f:
            f.write(string)
        f.close()

    def clear(self):
        if 'borrar todo' in self.__dictado__:
            string = ''
            with open(self.file, 'w', encoding='utf-8') as f:
                f.write(string)
            f.close()
