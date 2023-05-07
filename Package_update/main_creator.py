import os
import json

# Solicitar ruta del directorio
dir_path = input("Ingrese la ruta del directorio donde crear la estructura de carpetas y archivos: ")

# Crear directorios y archivos
os.makedirs(os.path.join(dir_path, "settings", "routes"), exist_ok=True)

# Crear archivo json en el directorio routes
data = {"exec": [[], []]}
with open(os.path.join(dir_path, "settings", "routes", "routes.json"), "w") as f:
    json.dump(data, f)

content = '''from General_Utilities.menu import menu

key = 'exec'
sub_key = ''
menu(
    key,
    sub_key
)
'''

# Crear archivo menu.py en el directorio raiz
with open(os.path.join(dir_path, "menu.py"), "w") as f:
    f.write(content)
