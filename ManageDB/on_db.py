# ---------------------------------------------------------------------
# ABAE-SAT-UT-SGO
# Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
# Actualización: 2022-08-13
#
#   Módulo genérico para la actualización de tabla de Bases de Datos.
#
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Importamos las librerías.
# ---------------------------------------------------------------------
import pandas as pd
import mysql.connector

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Conexiones y ejecución sobre la base de datos.
# ---------------------------------------------------------------------
def on_db(__base_datos__, __sql__):
    __mydb__ = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = __base_datos__
    )

    __mycursor__ = __mydb__.cursor()
    __mycursor__.execute(__sql__)

    if __sql__ == "SHOW TABLES":
        __s__ = []
        for __x__ in __mycursor__:
            __s__.append(__x__[0])
        return __s__

    if "INSERT INTO" in __sql__ or "DELETE FROM" in __sql__:
        __mydb__.commit()
    
    if "SELECT" in __sql__:
        __myresult__ = __mycursor__.fetchall()
        return __myresult__

    if "UPDATE" in __sql__:
        __mydb__.commit()
        print(__mycursor__.rowcount, "record(s) affected")

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Extracción de cabeceras.
# ---------------------------------------------------------------------
def extraer_cabecera(dataf):
    col_cabeceras = []

    for i in dataf.columns:
        col_cabeceras.append(i\
            .replace('(', '_')\
            .replace(')', '')\
            .replace('.', '')\
            .replace(' ', '')\
            .replace('/', '_')\
            .replace('-', '')\
            )

    return col_cabeceras

# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# Generar la parte de la orden sql para la inserción de las cabeceras.
# ---------------------------------------------------------------------
def sql_cabeceras(dataf):
    str_cabeceras_0 = ''
    
    for i in range(len(extraer_cabecera(dataf))):
        if i < len(extraer_cabecera(dataf)) - 1:
            str_cabeceras_0 = str_cabeceras_0 + '`' + extraer_cabecera(dataf)[i] + '`' + ', '
        if i == len(extraer_cabecera(dataf)) - 1:
            str_cabeceras_0 = str_cabeceras_0 + '`' + extraer_cabecera(dataf)[i] + '`'

    return '(`id`, ' + str_cabeceras_0 + ')'    

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Generar la parte de la orden sql para la inserción de los registros.
# ---------------------------------------------------------------------
def sql_registro(dataf, Num_reg):
    str_registro_0 = ''

    for i in range(len(dataf.iloc[Num_reg])):
        field_value = str(dataf.iloc[Num_reg][i]).replace('_x000D_', '')
        if i < len(dataf.iloc[Num_reg]) - 1:
            str_registro_0 = str_registro_0 + "'" + field_value + "'" + ', '
        if i == len(dataf.iloc[Num_reg]) - 1:
            str_registro_0 = str_registro_0 + "'" + field_value + "'"

    return '(NULL, ' + str_registro_0 + ')'

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Construir la orden sql para la inserción de registros con cabeceras.
# ---------------------------------------------------------------------
def sql_insert_generator(dataf, S_base_datos, S_tabla, Num_reg):
    return "INSERT INTO " + S_base_datos + "." + S_tabla + " \
    " + sql_cabeceras(dataf) + " VALUES \
    " + sql_registro(dataf, Num_reg) + ";"

# ---------------------------------------------------------------------



# ---------------------------------------------------------------------
# Método para inserción en la base de datos.
# ---------------------------------------------------------------------
def Insertar_registro_db(dataf, S_base_datos, S_tabla, Num_reg):
    sql = sql_insert_generator(dataf, S_base_datos, S_tabla, Num_reg)
    on_db(S_base_datos, sql)

def Insertar_registro_masivo(dataf, S_base_datos, S_tabla):
    for N_reg in range(len(dataf)):
        porcentaje = N_reg/(len(dataf) - 1)*100
        print('Registros insertados: {0:.0f}%'.format(porcentaje), end='\r')
        # Insertar_registro_db(dataf, S_base_datos, S_tabla, N_reg)
        sql = sql_insert_generator(dataf, S_base_datos, S_tabla, N_reg)
        on_db(S_base_datos, sql)

        reset_cont(S_base_datos, S_tabla)

# ---------------------------------------------------------------------



# ---------------------------------------------------------------------
# Método para actualizar los índices de la tabla.
# ---------------------------------------------------------------------
def reset_cont(S_base_datos, S_tabla):
    drop_id = "ALTER TABLE " + S_base_datos + "." + S_tabla + " \
        DROP COLUMN id"
    on_db(S_base_datos, drop_id)

    add_id = "ALTER TABLE " + S_base_datos + "." + S_tabla + " ADD \
    `id` BIGINT NOT NULL AUTO_INCREMENT FIRST, \
    ADD PRIMARY KEY (`id`);"
    on_db(S_base_datos, add_id)

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Extraer a DataFrame
# ---------------------------------------------------------------------
def mysql_extract_table_df(base_datos, tabla):
    sql1 = "SELECT * FROM " + tabla + ' PROCEDURE ANALYSE()'
    sql2 = "SELECT * FROM " + tabla

    data_columns = []
    esquema = on_db(base_datos, sql1)
    for i in range(len(esquema)):
        data_columns.append(str(esquema[i][0].split(b',')[0].split(b'.')[-1]).split("'")[1])

    df = pd.DataFrame(on_db(base_datos, sql2))
    df.columns = data_columns
    df['id'] = [i for i in range(len(df))]
    df.set_index('id',inplace=True)
    df.index.name = None

    return df

# ---------------------------------------------------------------------