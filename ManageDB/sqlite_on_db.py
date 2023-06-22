import pandas as pd
import sqlite3
from sqlite3 import Error
from General_Utilities.fecha import dttostr


def create_connection(__db__):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(__db__)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def show_tables(__db__):
	'''
	Muestra todas las tablas de la db especificada.
	'''

	# Conectarse a la base de datos
	conn = sqlite3.connect(__db__)

	# Crear un cursor
	cursor = conn.cursor()

	# Consulta SQL para obtener los nombres de las tablas
	query = "SELECT name FROM sqlite_master WHERE type='table';"

	# Ejecutar la consulta
	cursor.execute(query)

	# Obtener los resultados
	tables = cursor.fetchall()

	# # Imprimir los nombres de las tablas
	# for table in tables:
	# 	print(table[0])
	tables = [table[0] for table in tables]

	# Cerrar la conexión
	conn.close()

	return tables

def drop_table(__db__, __table__):
	conn =  sqlite3.connect(__db__)
	cursor = conn.cursor()
	sql = f"DROP TABLE IF EXISTS {__table__}"
	cursor.execute(sql)

def create_table(__db__, __table__, __dict__):

	campos = list(__dict__.keys())

	sql = f" CREATE TABLE {__table__}("

	for i in range(len(campos)):
		if i == 0:
			sql = sql + f"{campos[i]} INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
		elif i < len(campos) - 1:
			sql = sql + f"{campos[i]} {__dict__[campos[i]]}, "
		else:
			sql = sql + f"{campos[i]} {__dict__[campos[i]]});"

	conn = sqlite3.connect(__db__)
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.close()

def sql_inject(__db__, __sql__):
	conn = sqlite3.connect(__db__)
	cursor = conn.cursor()
	cursor.execute(__sql__)
	conn.close()

def reset_count(__db__, __table__, campo, a, b):
	__sql__ = 'UPDATE ' + __table__ + ' SET ' \
    f'"{campo}"={b} WHERE "{campo}"={a};'
	conn = sqlite3.connect(__db__)
	cursor = conn.cursor()
	cursor.execute(__sql__)
	conn.close()

def selectall(__db__, __table__):
	conn = sqlite3.connect(__db__)
	sql="SELECT * FROM " + __table__
	cursor=conn.execute(sql)	
	cabeceras = get_column_names(__db__, __table__)
	capturador=[]
	for fila in cursor:
		capturador.append(fila)
	conn.close()
	__dict__ = {}

	for i in range(len(cabeceras)):
		j_list = []
		for j in range(len(capturador)):
			j_list.append(capturador[j][i])
		__dict__[cabeceras[i]] = j_list		

	df = pd.DataFrame(__dict__)
	df = df.set_index('Id')
	return df

def selectall_id(__db__, __table__, id=None):
	conn = sqlite3.connect(__db__)
	sql="SELECT * FROM " + __table__
	cursor=conn.execute(sql)	
	cabeceras = get_column_names(__db__, __table__)
	capturador=[]
	for fila in cursor:
		capturador.append(fila)
	conn.close()
	__dict__ = {}

	for i in range(len(cabeceras)):
		j_list = []
		for j in range(len(capturador)):
			j_list.append(capturador[j][i])
		__dict__[cabeceras[i]] = j_list		

	df = pd.DataFrame(__dict__)
	if id==None:
		id='Id'
	df = df.set_index(id)
	return df
	
def selectone(__db__, __table__, __condition__):
	con=sqlite3.connect(__db__)
	sql="SELECT * FROM " + __table__ + \
	" WHERE " + __condition__
	cursor=con.execute(sql)	
	filas=cursor.fetchall()
	capturador=[]
	for fila in filas:
		capturador.append(fila)
	con.close()
	return(capturador)
	
def get_column_names(__db__, __table__):
	conn = sqlite3.connect(__db__)
	sql = "SELECT * FROM " + __table__
	cursor = conn.execute(sql)
	conn.close()
	column_names = [desc[0] for desc in cursor.description]
	return(tuple(column_names))

def insert(__db__, __table__, __val__):
	cabeceras=get_column_names(__db__, __table__)
	val_cab='('
	for i in cabeceras:
		val_cab=val_cab + ',?'
	val_cab=val_cab + ')'
	val_cab=val_cab.replace('(,?,','(')
	con=sqlite3.connect(__db__)
	sql="insert into " + __table__ + \
	str(cabeceras[1:]) + ' values ' + \
	val_cab #'(?,?)' #str(val_cab)
	con.execute(sql, __val__)
	con.commit()
	con.close()

def redef_tupla(__tupla__, index):
	'''
	Tomara las entradas de una tupla, y convertira la entrada especificada segun el valor del atributo "index" en una string con el formato arrojado por "FechaID".
	'''
	# from General_Utilities.fecha import dttostr
	N_tupla = []

	for i in range(len(__tupla__)):
		j = __tupla__[i]
		if i == index:
			N_tupla.append(dttostr(j))
		elif i != index:
			N_tupla.append(j)        
	
	N_tupla = tuple(N_tupla)

	return N_tupla

def sqlite_Insertar_registro_masivo(__db__, __table__, __df__, __start_index__, __temp_ind__):
	'''
	Inserta masivamente los datos de un dataframe, convirtiendo los datos de tipo datetime a string de la columna de indice __temp_ind__.
	'''
	for i in range(len(__df__)):
		tupla = tuple(__df__.iloc[i])[__start_index__:]
		rows = redef_tupla(tupla, __temp_ind__)
		# print(rows)
		avance = (i / len(__df__)) * 100
		print(avance, end='\r')
		insert(__db__, __table__, rows)

def sqlite_Insertar_df_masivo(__db__, __table__, __df__):
	'''
	Inserta masivamente los datos de un dataframe, convirtiendo los datos de tipo datetime a string de la columna de indice __temp_ind__.
	'''
	for i in range(len(__df__)):
		tupla = tuple(__df__.iloc[i])
		rows = tupla
		# print(rows)
		avance = (i / len(__df__)) * 100
		print(avance, end='\r')
		insert(__db__, __table__, rows)