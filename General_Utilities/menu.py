import subprocess
from General_Utilities.object_utils import request, get_method_tags
from General_Utilities.option_list import option_list
from General_Utilities.control_rutas import setting_routes


def menu_class(cls):

	while True:

		subprocess.run('clear', shell=True)
		tags = get_method_tags(cls)
		opciones, acciones = [i[1] for i in tags], [i[0] for i in tags]

		opciones.append("Salir")
		opcion = option_list(opciones)

		for i in range(len(opciones)):
			if opcion == opciones[i]:
				j = i

		if j < len(opciones) - 1:
			endpoint = acciones[j]
			request(cls, endpoint)

		elif j == len(opciones) - 1:
			print('Adios!')
			break
		else:
			print('\nOpcion Invalida! Repita la seleccion.\n')

		input('Presione una tecla para continuar: ')



def menu(
		key: str,
		sub_key: str
	):

	'''
	Funcion para levantar menu automatico con las opciones configuradas en el archivo routes.json.

	*parameters:
		key: str. Clave de acceso a las opciones. Por defecto key deberia ser "exec".
		sub_key: str. Si key == "sub_exec", se acceden a opciones de submenu.

	'''

	while True:

		# subprocess.run('cls', shell=True)
		subprocess.run('clear', shell=True)

		if key == 'exec':
			opciones = setting_routes(key)[0]
			acciones = setting_routes(key)[1]
		elif key == 'sub_exec':
			opciones = setting_routes(key)[sub_key]['opciones']
			acciones = setting_routes(key)[sub_key]['acciones']

		opciones.append("Salir")

		opcion = option_list(opciones)

		for i in range(len(opciones)):
			if opcion == opciones[i]:
				j = i

		if j < len(opciones) - 1:
			exec(open(acciones[j]).read())
		elif j == len(opciones) - 1:
			print('Adios!')
			break
		else:
			print('\nOpcion Invalida! Repita la eleccion.\n')
			# exec(open("menu.py").read())
		
		input('Presione una tecla para continuar: ')