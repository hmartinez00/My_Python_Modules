# import webbrowser
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Hola soy tu asistente de voz: ')
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print(f'Haz dicho: {text}')
    print(text)
except:
    print('No te he entendido')