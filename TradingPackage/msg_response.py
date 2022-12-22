class strmsg:
    
    def __init__(
        self,
        __method_name__,
        __tuple__
    ):
        self.__method_name__ = __method_name__
        self.__tuple__ = __tuple__

    def msg(self):
        if self.__method_name__ == 'trading_latino':

            tupla = self.__tuple__
            moment = tupla[0]
            actual_price = tupla[2]
            ema10 = tupla[3]
            ema55 = tupla[4]
            adx1 = tupla[5]
            squeeze1 = tupla[6]
            adx2 = tupla[7]
            squeeze2 = tupla[8]

            response = \
f'''{moment}

actual_price: {actual_price:.2f}, ema10: {ema10:.2f}, ema55: {ema55:.2f}
squeeze.iloc[-1]: {squeeze1:.2f}, adx.iloc[-1]: {adx1:.2f}
squeeze.iloc[-2]: {squeeze2:.2f}, adx.iloc[-2]: {adx2:.2f}

Delta10_actual_price: {ema10 - actual_price:.2f}, Delta55_actual_price: {ema55 - actual_price:.2f}
Delta_emas: {ema10 - ema55:.2f}, Delta_squeeze: {squeeze1 - squeeze2:.2f}, Delta_adx: {adx1 - adx2:.2f}
'''
            return response