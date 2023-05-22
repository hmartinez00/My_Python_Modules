import re
import inspect


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