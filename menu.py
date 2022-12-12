import subprocess
from General_Utilities.option_list import option_list

subprocess.run('clear')

opciones=[
	'Generar Setup',
	'Actualizar Proyecto',
	'Salir',
]

opcion = option_list(opciones)

if opcion==opciones[0]:
	exec(open("Package_update/setup_generator.py").read())
elif opcion==opciones[1]:
	exec(open("Package_update/builder.py").read())
elif opcion==opciones[2]:
	print('Adios!')
else:
	print('\nOpcion Invalida! Repita la eleccion.\n')
	exec(open("menu.py").read())