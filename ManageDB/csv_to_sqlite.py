import pandas as pd
from ManageDB.mysql_on_db import extraer_cabecera
from ManageDB.sqlite_on_db import create_connection, drop_table, create_table, selectall, sqlite_Insertar_df_masivo


base_datos = r'C:\Users\admin\Documents\0 - A Control de Procesos\data\vrss_operation_and_managment_subsystem'
tabla = '`guardias`'

file = r'C:\Users\admin\Documents\distribucion_de_guardias_ut_2023_2024.csv'
df = pd.read_csv(file)
# df['Id'] = [i for i in range(len(df))]
df.set_index('Id',inplace=True)
df.index.name = None
print(df)

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
sqlite_Insertar_df_masivo(base_datos, tabla, df)
print(selectall(base_datos, tabla))