from datetime import datetime, timedelta, date


def dttostr(__dt__):
	'''
	Toma una dato datetime y lo convierte en una cadena arrojando
	la fecha en formato yymmdd.
	'''
	__fecha__ = datetime.strftime(
		__dt__
		, '%Y-%m-%d %H:%M:%S'
	)
	
	return(__fecha__)

def BatchID(__dt__):
	'''
	Toma una dato datetime y lo convierte en una cadena arrojando
	la fecha en formato yymmdd.
	'''
	__fecha__ = datetime.strftime(
		__dt__
		, '%Y%m%d'
	)
	
	return(__fecha__)
	
def FechaID(__dt__):
	__fecha__ = datetime.strftime(
		__dt__
		, '%Y-%m-%d'
	)
	
	return(__fecha__)

def DeltaT(__strdt__, __delay__):
	__fecha__ = datetime.strftime(
		datetime.strptime(
			__strdt__, '%Y-%m-%d'
		) - timedelta(days=int(__delay__))
		, '%Y-%m-%d'
	)
	
	return(__fecha__)

def TimeID(__dt__):
	__fecha__ = datetime.strftime(
		__dt__
		, '%H%M%S'
	)
	
	return(__fecha__)
	
def HoraID(__dt__):
	__fecha__ = datetime.strftime(
		__dt__
		, '%H:%M'
	)
	
	return(__fecha__)

def format_FechaID(__strdt__):
	__fecha__ = datetime.strftime(
		datetime.strptime(
			__strdt__, '%Y%m%d'
		), '%Y-%m-%d'
	)

	return(__fecha__)

def date_fechaID(__strdt__):
	__fecha__ = datetime.strptime(
			__strdt__, '%Y%m%d'
		).date()

	return(__fecha__)

def f_timestamp(__timestamp__):
	'''
	convert the timestamp to a datetime object in the local timezone
	'''
	dt_object = datetime.fromtimestamp(__timestamp__)

	return dt_object

def t_timestamp(__dt__):
	'''
	convert the datetime to a timestamp object in the local timezone
	'''
	dt_object = __dt__.timestamp()

	return dt_object