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

    def close_options(self, __list__):
        if self.__dictado__ in __list__:           
            return True

    def secuence_options(self, __list__):

        value = False
        for i in range(len(__list__)):
            if self.__dictado__ == __list__[i][0]:
                value = True
        
        if value == True:
            string = self.string + __list__[i][1]
                    # if i == 0:
                    #     string = self.string + '\n'
                    # elif i == 1:
                    #     string = self.string + '\n\n'
       
        else:
            string = self.string + ' ' + str(self.__dictado__)
        # print(
        #         self.__dictado__ in __list__
        #     )
        
        with open(self.file, 'w', encoding='utf-8') as f:
            f.write(string)
        f.close()

    def clear(self, __list__):
        if self.__dictado__ in __list__:
            string = ''
            with open(self.file, 'w', encoding='utf-8') as f:
                f.write(string)
            f.close()
