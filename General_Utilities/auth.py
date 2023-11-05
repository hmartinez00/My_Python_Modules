from ManageDB.mysql_on_db import mysql_extract_table_df
import pandas as pd


class Auth():

    def __init__(self):
        self.base_datos = 'trades'
        self.tabla = 'claves'

    def auth(self, __i__):
        data = mysql_extract_table_df(self.base_datos, self.tabla)
        info = data.iloc[__i__]

        return info
