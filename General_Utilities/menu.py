import subprocess
import inspect
import re
from General_Utilities.option_list import option_list
from General_Utilities.control_rutas import setting_routes


def request(cls, endpoint: str, parameters: dict = None):
	'''
	Metodo de control de errores.
	
	Envia la peticion del endpoint (metodos especificos de la API como time, account, ticker_price, etc...), y devuelve la respuesta, ya se sin parametros o con parametros y en caso de que ocurra un error, controla el error.

	En caso de necesitarse parametros para endpint, o metodos propios de Api, se deben introducir mediante un diccionario. Lo veremos con los objetos llamados "params" en varios de los metodos de la clase.
	'''
	
	try:
		response = getattr(cls, endpoint) # => self.binance_client.endpoint
		return response() if parameters is None else response(**parameters)
	except:
		response()
		print(f'El endpoint "{endpoint}" ha fallado. \n\nParametros: {parameters}')


def get_method_tags(cls):
	"""
	Escanea un objeto de clase y retorna una lista con las etiquetas y descripciones resumidas de sus métodos.

	:param cls: Objeto de clase a escanear.
	:return: Lista de etiquetas y descripciones resumidas de los métodos.
	"""
	tags = []
	for name, method in inspect.getmembers(cls, inspect.ismethod):
		docstring = inspect.getdoc(method)
		if docstring:
			match = re.search(r"main_description:\s*(.*)", docstring)
			if match:
				description = match.group(1)
				tags.append((name, description))
	return tags

def menu_class(cls):

	# out = []

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
			# out.append(endpoint)
			request(cls, endpoint)
		elif j == len(opciones) - 1:
			print('Adios!')
			break
		else:
			print('\nOpcion Invalida! Repita la eleccion.\n')
	
	# return out


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
	else:
		print('\nOpcion Invalida! Repita la eleccion.\n')
		exec(open("menu.py").read())