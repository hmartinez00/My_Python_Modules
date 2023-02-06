from datetime import datetime as dt
from TradingPackage.Fbinance import Future_Binancebot as Finfo
from TradingPackage.Indicators import Indicators as ind
from TradingPackage.msg_response import strmsg


class set_values:


    def __init__(
            self,
            pair,
            temporality,
        ):

        self.pair = pair
        self.temporality = temporality

    def trading_latino(self):

        bot = Finfo(
            self.pair,
            self.temporality,
        )

        df = ind(bot.candlesticks())

        moment, actual_price, ema10, ema55, adx, squeeze = (
                dt.strftime(
                    dt.now(), '%Y-%m-%d %H:%M:%S'
                ),
                bot.symbol_price(), 
                df.ema(10).iloc[-1],
                df.ema(50).iloc[-1],
                df.adx(),
                # df.macd_lazybear(),
                df.lazybear(),
            )
    
        if actual_price > ema10 and actual_price > ema55 and adx.iloc[-1] > adx.iloc[-2] and squeeze.iloc[-1] > squeeze.iloc[-2]:
            condiciones = 'Condiciones para el alza!'
        else:
            condiciones = 'No hay condiciones.'

        respuesta = moment, condiciones, actual_price, ema10, ema55, adx.iloc[-1], squeeze.iloc[-1], adx.iloc[-2], squeeze.iloc[-2]

        msg = strmsg(
            'trading_latino',
            respuesta
        ).msg()

        return respuesta, msg

    def strategy_cci(self):
        
        bot = Finfo(
            self.pair,
            self.temporality,
        )

        df = ind(bot.candlesticks())

        moment, actual_price, cci = (
            dt.strftime(
                dt.now(), '%Y-%m-%d %H:%M:%S'
            ),
            round(bot.symbol_price(), 2), 
            round(df.cci().iloc[-1],2),
        )

        if cci > 100:
            condicion = 'COMPRA!'
        elif cci < -100:
            condicion = 'VENTA!'
        else:
            condicion = ''

        respuesta = (
                moment,
                actual_price,
                cci,
                condicion
            )

        msg = strmsg(
            'strategy_cci',
            respuesta
        ).msg()

        return respuesta, msg

    def strategy_macd(self):
        
        bot = Finfo(
            self.pair,
            self.temporality,
        )

        df = ind(bot.candlesticks()).macd().iloc[-1]

        moment, actual_price, macd, signal, histo = (
            dt.strftime(
                    dt.now(), '%Y-%m-%d %H:%M:%S'
                ),
            bot.symbol_price(),
            df.get('MACD_12_26_9'),
            df.get('MACDs_12_26_9'),
            df.get('MACDh_12_26_9'),
        )

        condiciones = ''

        respuesta = moment, condiciones, actual_price, macd, signal, histo

        return respuesta