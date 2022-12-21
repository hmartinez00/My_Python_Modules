# Author: Ronny Portillo


import pandas_ta as ta
import numpy as np
from TradingPackage.Special_Indicators import Sind as sta


class Indicators:

    def __init__(self, data):
        self.df = data
        self.Close = self.df.get('Close')
        self.High = self.df.get('High')
        self.Low = self.df.get('Low')
        self.EMATP = 9
        self.RSITP = 14
        self.CCITP = 20
        self.MACD_period_fast = 12
        self.MACD_period_slow = 26
        self.MACD_signal = 9

    def ema(
                self,
                timeperiod: int = None,
            ):
        '''
        Devuelve la Media Movil Exponencial del DataFrame de las velas.
        '''

        timeperiod = self.EMATP if timeperiod is None else timeperiod

        return ta.ema(
                    self.Close, 
                    timeperiod
                )

    def rsi(
                self,
                timeperiod: int = None,
            ):
        '''
        Devuelve la Media Movil Exponencial del DataFrame de las velas.
        '''

        timeperiod = self.RSITP if timeperiod is None else timeperiod

        return ta.rsi(
                    self.Close, 
                    timeperiod
                )

    def cci(
                self,
                timeperiod: int = None,
            ):
        '''
        Devuelve Commodity Chanel Index.
        '''

        timeperiod = self.CCITP if timeperiod is None else timeperiod

        return ta.cci(
                    self.Close, 
                    timeperiod
                )

    def macd(
                self,
                period_fast: int = None,
                period_slow: int = None,
                signal: int = None,
            ):
        '''
        Devuelve la Media Movil Exponencial del DataFrame de las velas.
        '''

        period_fast = self.MACD_period_fast if period_fast is None else period_fast
        period_slow = self.MACD_period_slow if period_slow is None else period_slow
        signal = self.MACD_signal if signal is None else signal

        return ta.macd(
                self.Close, 
                period_fast,
                period_slow,
                signal,
            )

    def adx(self):
        return ta.adx(
                self.High,
                self.Low,
                self.Close,
        ).get('ADX_14')
    
    def macd_lazybear(self):
       
        squeeze = ta.squeeze(
            self.High,
            self.Low,
            self.Close,
            lazybear=True
        )

        squeeze.columns = [
            'SQZ', 
            'SQZ_ON',
            'SQZ_OFF',
            'SQZ_NO'
        ]

        return squeeze.get('SQZ')

    def lazybear(self):
       
        squeeze = sta(self.df).lazybear()

        return squeeze