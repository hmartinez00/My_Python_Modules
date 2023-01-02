from datetime import datetime, timedelta

def BatchID(__dt__):
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