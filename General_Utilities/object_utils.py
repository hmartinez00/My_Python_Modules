import re
import inspect


def request(cls, endpoint: str, parameters: dict = None):
	'''
	Permite aplicar un metodo a un objeto de clase usando el nombre del metodo en formato str. Esta basada en basada en getattr(), y devuelve la respuesta, ya se sin parametros o con parametros y en caso de que ocurra un error, controla el error.

	En caso de necesitarse parametros para metodo, se deben introducir mediante un diccionario.
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