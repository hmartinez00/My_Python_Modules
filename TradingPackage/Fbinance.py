# Author: Ronny Portillo

from binance.um_futures import UMFutures
import pandas as pd
import numpy as np
from datetime import datetime as dt
from General_Utilities.auth import Auth


class Future_Binancebot:

    data = Auth().auth('binance')
    __api_key = data[2]
    __api_secret = data[3]

    
    binance_client = UMFutures(key=__api_key, secret=__api_secret)

    def __init__(
            self, 
            pair: str, 
            temporality: str
        ):
        self.pair = pair.upper()
        self.temporality = temporality
        self.symbol = self.pair.split('USDT')[0]

    def _request(self, endpoint: str, parameters: dict = None):
        '''
        Metodo de control de errores.
        
        Envia la peticion del endpoint (metodos especificos de la API como time, account, ticker_price, etc...), y devuelve la respuesta, ya se sin parametros o con parametros y en caso de que ocurra un error, controla el error.

        En caso de necesitarse parametros para endpint, o metodos propios de Api, se deben introducir mediante un diccionario. Lo veremos con los objetos llamados "params" en varios de los metodos de la clase.
        '''
        
        try:
            response = getattr(self.binance_client, endpoint) # => self.binance_client.endpoint
            return response() if parameters is None else response(**parameters)
        except:
            response()
            print(f'El endpoint "{endpoint}" ha fallado. \n\nParametros: {parameters}')


    def binance_time(self):
        '''
        Devuelve el tiempo del servidor de binance
        '''

        server = self._request('time').get('serverTime')

        return server
    
    def binance_account(self) -> dict:
        '''
        Devuelve metricas asociadas a la cuenta.
        '''

        return self._request('account')

    def cryptocurrencies(self) -> list:
        '''
        Devuelve una lista de todas las cryptos que tienen saldo positivo
        '''

        # return [crypto for crypto in self.binance_account().get('balance') if float(crypto.get('free')) > 0]
        return self.binance_account().get('totalWalletBalance')

    def symbol_price(self, pair: str = None):
        '''
        Devuelve el valor de la paridad

        param pair: Par que se desea contrastar
        return: Precio
        '''

        symbol = self.pair if pair is None else pair

        params = {
                'symbol': symbol.upper()
            }

        return float(self._request('ticker_price', params).get('price'))
    
    def candlesticks(self, limit: int = 500) -> pd.DataFrame:

        '''
        Devuelve las velas japonesas
        '''

        params = {
            'symbol': self.pair,
            'interval': self.temporality,
            'limit': limit          
        }

        candle = pd.DataFrame(
            self._request('klines', params),

            columns = [
                'Kline Open time',
                'Open',
                'High',
                'Low',
                'Close',
                'Volume',
                'Kline Close time',
                'Quote asset volume',
                'Number of trades',
                'Taker buy base asset volume',
                'Taker buy quote asset volume',
                'Unused field, ignore',
            ],

            dtype=np.float64
        )
        

        candle['Kline Open time'] = pd.Series([dt.fromtimestamp(i) for i in candle['Kline Open time'] / 1000])
        candle['Kline Close time'] = pd.Series([dt.fromtimestamp(i) for i in candle['Kline Close time'] / 1000])

        candle = candle.set_index('Kline Open time')

        return candle[
            [
                'Open',
                'High',
                'Low',
                'Close',
                'Volume',
            ]
        ]

    def f_order(self, __order__):

        '''
        Abre una orden
        '''
        params = __order__       

        self._request('new_order', params)