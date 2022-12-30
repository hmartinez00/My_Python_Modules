# Puede requerir previamente pipwin
# y pipwin install pyaudio
import speech_recognition as sr

def Reconocimiento():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Te escucho: ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="es-ES")
        # print(f'Haz dicho: {text}')
    except:
        print('No te he entendido')

    return text