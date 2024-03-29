# pip install speechrecognition
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

    def close_options(self, __list__):
        if self.__dictado__ in __list__:        
            return True

    def secuence_options(self, __list__A, __list__B):
       
        if self.__dictado__ in __list__A:        
            for i in range(len(__list__A)):
                if self.__dictado__ == __list__A[i]:
                    j = i

            string = self.string + __list__B[j]
       
        else:
            string = self.string + ' ' + str(self.__dictado__)
        
        with open(self.file, 'w', encoding='utf-8') as f:
            f.write(string)
        f.close()

    def clear(self, __list__):
        if self.__dictado__ in __list__:
            string = ''
            with open(self.file, 'w', encoding='utf-8') as f:
                f.write(string)
            f.close()
