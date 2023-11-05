from ManageDB.mysql_on_db import mysql_extract_table_df
import pandas as pd

def auth(__i__):
    base_datos = 'trades'
    tabla = 'claves'
    data = mysql_extract_table_df(base_datos, tabla)
    info = data.iloc[__i__]

    return info
