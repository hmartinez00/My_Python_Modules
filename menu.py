import os
import subprocess
from General_Utilities.option_list import option_list

subprocess.run('clear')

opciones=[
	'Crear paquete vacio',
	'Actualizar un paquete',
	'Actualizar todos los paquetes',
	'Salir',
]

opcion = option_list(opciones)

if opcion==opciones[0]:
	exec(open("Package_update/builder.py").read())
elif opcion==opciones[1]:
	exec(open("Package_update/single_updater.py").read())
elif opcion==opciones[2]:
	exec(open("Package_update/full_updater.py").read())
elif opcion==opciones[3]:
	print('Adios!')
else:
	print('\nOpcion Invalida! Repita la eleccion.\n')
	exec(open("menu.py").read())