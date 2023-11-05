from ManageDB.mysql_on_db import mysql_extract_table_df
import pandas as pd


class Auth():

    def __init__(self):
        self.base_datos = 'trades'
        self.tabla = 'claves'

    def df_auth(self, __i__):
        data = mysql_extract_table_df(self.base_datos, self.tabla)
        info = data[data['field1'] == __i__]

        return info

    def auth(self, __i__):
        info = self.df_auth(__i__).values.tolist()[0]

        return info
