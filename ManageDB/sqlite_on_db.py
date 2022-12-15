import pandas as pd
import sqlite3
from sqlite3 import Error


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

def reset_count(__db__, __table__):
	add_id = 'UPDATE ' + __table__ + ' SET ' \
    '"Id"=20 WHERE "Id"=2;'
	sql_inject(__db__, add_id)

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