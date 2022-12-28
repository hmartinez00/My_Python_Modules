import pandas as pd
import numpy as np


class Sind:      

    def __init__(self, data):
        self.df = data
        self.Open = self.df.get('Open')
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


    def critical_points(self):

        Cierre = self.Close
        Apertura = self.Open
        critical = [[False, False] for i in range(len(Cierre))]

        for i in range(len(Cierre)):

            if i > 0 and i < len(Cierre) - 1:
                if \
                    Cierre[i] > Cierre[i-1] and \
                    Cierre[i] > Apertura[i-1] and \
                    Cierre[i] > Cierre[i+1] and \
                    Cierre[i] > Apertura[i+1]:
                    critical[i][0] = Cierre[i]

                if \
                    Cierre[i] < Cierre[i-1] and \
                    Cierre[i] < Apertura[i-1] and \
                    Cierre[i] < Cierre[i+1] and \
                    Cierre[i] < Apertura[i+1]:
                    critical[i][1] = Cierre[i]

                if \
                    Apertura[i] > Cierre[i-1] and \
                    Apertura[i] > Apertura[i-1] and \
                    Apertura[i] > Cierre[i+1] and \
                    Apertura[i] > Apertura[i+1]:
                    critical[i][0] = Apertura[i]

                if \
                    Apertura[i] < Cierre[i-1] and \
                    Apertura[i] < Apertura[i-1] and \
                    Apertura[i] < Cierre[i+1] and \
                    Apertura[i] < Apertura[i+1]:
                    critical[i][1] = Apertura[i]

        dataf = pd.DataFrame(
                critical,
                columns=['Max', 'Min']
            )

        return dataf
    
    def filter(self, values):
        #------------------------------------------------------------
        # CRITERIOS
        #------------------------------------------------------------
        # Existen algunas reglas empíricas que podemos emplear para
        # la detección de niveles críticos notables.

        #------------------------------------------------------------
        #1. Regla del MULTIPLE RECHAZO: 
        #------------------------------------------------------------
        # Los niveles deben estar confirmados por multiples rechazos.

        #------------------------------------------------------------
        #2. Regla del ALEJAMIENTO DRÁSTICO: 
        #------------------------------------------------------------
        # El precio debe alejarse drásticamente del máximo o mínimo.

        #------------------------------------------------------------
        #3. Regla de CERCANÍA AL PRECIO:
        #------------------------------------------------------------
        # Los niveles tienen que estar cercanos al precio actual, i.e; 
        # (cierre de la ultima vela).

        actual_price = self.Close.iloc[-1]
        
        Graph_dev = pd.Series([abs(actual_price - i) for i in values if i != False])
        Graph_dev = Graph_dev.sort_values(ascending = True).reset_index().iloc[:,1]
        
        print(Graph_dev)

        # CRITERIOS
        #1. MULTIPLE RECHAZO.


        #2. ALEJAMIENTO DRÁSTICO.


        #3. CERCANÍA AL PRECIO.
        Graph_list = []
        for i in values:
            if i != False:
                for j in range(3):
                    if abs(actual_price - i) == Graph_dev.iloc[j]:
                        Graph_list.append(i)

        

        return Graph_list


    def Res(self):
        values = self.critical_points()['Max']
        Graph_list = self.filter(values)

        return Graph_list

    def Sup(self):
        values = self.critical_points()['Min']
        Graph_list = self.filter(values)        

        return Graph_list