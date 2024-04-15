# Importamos Gemini Pro, textwrap, IPython, sys, para soporte Para Caracteres Especiales en la Terminal de Python 
import google.generativeai as genai 
import textwrap 
from IPython.display import Markdown 
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
 
# Usamos el modelo generativo de la IA 
modelo = genai.GenerativeModel('gemini-pro')

# Abrir el archivo JSON
with open('settings.json', 'r') as f:
    data = json.load(f)

# Configuramos la API KEY 
GOOGLE_API_KEY=data['api']
genai.configure(api_key=GOOGLE_API_KEY)
 
# Rebajamos el tamaño de la respuesta de la IA 
def rebajar(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Abrir el archivo en modo lectura
with open('quest.md', 'r', encoding='utf-8') as archivo:
    # Leer el contenido del archivo
    quest = archivo.read()

# quest = "Crea un codigo que me permita leer y copiar el contenido de un archivo de texto con python."

# Obtenemos la respuesta 
respuesta = modelo.generate_content(quest)
respuesta = respuesta.text

with open('ask.md', 'w', encoding='utf-8') as f:
    f.writelines(respuesta)

# Imprimimos la respuesta 
# print(respuesta)