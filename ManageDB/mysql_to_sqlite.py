from ManageDB.mysql_on_db import mysql_extract_table_df, extraer_cabecera
from ManageDB.sqlite_on_db import create_connection, drop_table, redef_tupla, create_table, selectall, sqlite_Insertar_registro_masivo


base_datos = 'vrss_operation_and_managment_subsystem'
tabla = '`distribucion_de_guardias_ut_2023_2024`'

# Aca extraemos la tabla y la presentamos en un dataframe.
df = mysql_extract_table_df(base_datos, tabla)
# Tambien extraemos las cabeceras
cabeceras = extraer_cabecera(df)

# Construimos el diccionario de campos
dicc = {}
dicc['Id'] = 'PRIMARY'
for i in cabeceras:
    dicc[i] = 'TEXT'
print(dicc)

# Procedemos a construir la base de datos y agregar la tabla
create_connection(base_datos)
drop_table(base_datos, tabla)
create_table(base_datos, tabla, dicc)
sqlite_Insertar_registro_masivo(base_datos, tabla, df, 0, 4)
print(selectall(base_datos, tabla))