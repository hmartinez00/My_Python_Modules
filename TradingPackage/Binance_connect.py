import json
from binance.um_futures import UMFutures
from General_Utilities.control_rutas import setting_routes


class binance_client:

    def __init__(self):
        
        key = 'api'

        ruta_archivo_json = setting_routes(key)[0]
        with open(ruta_archivo_json) as archivo_json:
            datos_json = json.load(archivo_json)

        self.key = 'api'
        self.__api_key__ = datos_json['API_KEY']
        self.__api_secret__ = datos_json['API_SECRET']
    
        B_connection = UMFutures(key=self.__api_key__, secret=self.__api_secret__)

        return B_connection