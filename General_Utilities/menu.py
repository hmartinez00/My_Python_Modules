import subprocess
from General_Utilities.option_list import option_list
from General_Utilities.control_rutas import setting_routes


subprocess.run('cls', shell=True)

key = 'exec'
opciones = setting_routes(key)[0]
acciones = setting_routes(key)[1]
opciones.append("Salir")

opcion = option_list(opciones)

for i in range(len(opciones)):
	if opcion == opciones[i]:
		j = i

if j < len(opciones) - 1:
	exec(open(acciones[j]).read())
elif j == len(opciones) - 1:
	print('Adios!')
else:
	print('\nOpcion Invalida! Repita la eleccion.\n')
	exec(open("menu.py").read())