import pandas as pd
import numpy as np


class Sind:      

    def __init__(self, data):
        self.df = data
        self.Close = self.df.get('Close')
        self.High = self.df.get('High')
        self.Low = self.df.get('Low')
        self.EMATP = 9
        self.RSITP = 14
        self.MACD_period_fast = 12
        self.MACD_period_slow = 26
        self.MACD_signal = 9

    def lazybear(self):
        length = 20
        mult = 2.0
        length_KC = 20
        mult_KC = 1.5

        # Calculate Bollinger Bands
        m_avg = self.Close.rolling(window=length).mean()
        m_std = self.Close.rolling(window=length).std(ddof=0) * mult # mult_KC
        self.df['upper_BB'] = m_avg + m_std
        self.df['lower_BB'] = m_avg - m_std

        # Calculate True Range
        self.df['tr0'] = abs(self.High - self.Low)
        self.df['tr1'] = abs(self.High - self.Close.shift())
        self.df['tr2'] = abs(self.Low - self.Close.shift())
        self.df['tr'] = self.df[['tr0', 'tr1', 'tr2']].max(axis=1)

        # Calculate Kelner Channel
        range_ma = self.df['tr'].rolling(window=length_KC).mean()
        self.df['upper_KC'] = m_avg + range_ma * mult_KC
        self.df['lower_KC'] = m_avg - range_ma * mult_KC

        # Calculate
        highest = self.High.rolling(window=length_KC).max()
        lowest = self.Low.rolling(window=length_KC).min()
        m1 = (highest + lowest) / 2
        self.df['SQZ'] = self.Close - (m1 + m_avg) / 2
        y = np.array(range(0, length_KC))
        func = lambda x: np.polyfit(y, x, 1)[0] * (length_KC - 1) + np.polyfit(y, x, 1)[1]
        self.df['SQZ'] = self.df['SQZ'].rolling(window=length_KC).apply(func, raw=True)

        return self.df['SQZ']