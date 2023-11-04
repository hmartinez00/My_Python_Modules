import json
from binance.spot import Spot
from binance.um_futures import UMFutures
from General_Utilities.control_rutas import setting_routes
from ManageDB.mysql_on_db import mysql_extract_table_df


class binance_client:

    def __init__(self):
        
        # key = 'api'
        # ruta_archivo_json = setting_routes(key)[0]
        # with open(ruta_archivo_json) as archivo_json:
        #     datos_json = json.load(archivo_json)

        # self.key = 'api'
        # self.__api_key__ = datos_json['API_KEY']
        # self.__api_secret__ = datos_json['API_SECRET']

        base_datos = 'trades'
        tabla = 'claves'
        data = mysql_extract_table_df(base_datos, tabla)
        self.__api_key__ = data.iloc[1][2]
        self.__api_secret__ = data.iloc[1][3]

    def spot(self):
        B_connection = Spot(key=self.__api_key__, secret=self.__api_secret__)    
        return B_connection

    def futures(self):
        B_connection = UMFutures(key=self.__api_key__, secret=self.__api_secret__)
        return B_connection

