from TradingPackage.Bbinance import Binancebot as info
from TradingPackage.Indicators import Indicators as ind
import matplotlib.pyplot as plt
import mplfinance as mpf
from market_profile import MarketProfile


class set_plot:

    def __init__(
            self,
            pair,
            temporality,
        ):

        self.pair = pair
        self.temporality = temporality

    def trading_latino_plot(self, show = False):

        bot = info(
            self.pair,
            self.temporality,
        )

        df = bot.candlesticks()

        # Definiendo set de colores
        Titulo = "Estrategia TradingLatino"
        sub_title1 = 'EMA10 y EMA55'
        sub_title2 = 'ADX y Squeeze Lazybear'
        Label_Graph1 = 'EMA10'
        Label_Graph2 = 'EMA55'
        Label_Graph3 = 'ADX'
        Label_Graph4 = 'Lazybear'
        LabelY = 'Price'
        file = 'plots/status.png'
        fondo = '#161A25'
        contraste = 'white'
        color_Graph1 = '#2962FF'
        color_Graph2 = '#FF6229'
        verde_claro = '#0A9711'
        verde_oscuro = '#0A5111'
        rojo_claro = '#AA1C20'
        rojo_oscuro = '#520B10'
        letras = '#9598A1'
        
        # Definiendo conjuntos a graficar
        mp = MarketProfile(df)
        mp_slice = mp[df.index.min():df.index.max()]
        keys = mp_slice.profile.index.tolist()
        valores = mp_slice.profile.values.tolist()

        _adx = ind(df).adx()
        _squeeze = ind(df).lazybear()

        # Especificaciones generales de las graficas
        fig, ax = plt.subplots(2)
        mpf.plot(df, ax = ax[0], ema = (10, 55), type='candle', style='charles', mavcolors = [color_Graph1, color_Graph2])
        fig.set_facecolor(fondo)

        # Graficando funcion 1
        ax[0].set_ylabel(LabelY)
        ax[0].set_facecolor(fondo) #fondo
        ax[0].tick_params(colors=letras)
        ax[0].yaxis.label.set_color(letras)
        ax[0].xaxis.label.set_color(letras)

        # Graficando funcion 2
        # ax[0].plot(x, Graph2, color=color_Graph2, label=Label_Graph2, alpha=0.3)
        # # ax[0].set_ylabel(LabelY)
        # ax[0].set_facecolor(fondo) #fondo
        # ax[0].tick_params(colors=letras)
        # ax[0].yaxis.label.set_color(letras)
        # ax[0].xaxis.label.set_color(letras)
        
        ax[0].grid(linestyle='--', alpha=0.3)

        # Intercalando Barras
        ax1 = ax[0].twiny()
        ax1.barh(keys, valores, alpha=0.3)
        ax1.tick_params(colors=letras)


        # Graficando funcion 3
        ax[1].plot(_adx, color=contraste, label=Label_Graph3, alpha=0.7,)
        ax[1].axhline(y=23, color=contraste, linestyle='-.', alpha=0.7)
        ax[1].set_ylabel(Label_Graph3)
        ax[1].set_facecolor(fondo) #fondo
        ax[1].tick_params(colors=letras)
        ax[1].yaxis.label.set_color(letras)
        ax[1].xaxis.label.set_color(letras)
        ax[1].legend(loc='upper left', facecolor=contraste, edgecolor=contraste)

        # Intercalando Squeeze
        ax2 = ax[1].twinx()
        ax[1].set_zorder(ax2.get_zorder() + 1)
        ax[1].patch.set_visible(False)
        fig.set_facecolor(fondo)

        # Graficando funcion 4
        ax2.plot(_squeeze, color=contraste, label=Label_Graph4, alpha=0.3)
        ax2.set_ylabel(Label_Graph4)
        ax2.set_facecolor(fondo) #fondo
        ax2.tick_params(colors=letras)
        ax2.yaxis.label.set_color(letras)
        ax2.xaxis.label.set_color(letras)
        # ax2.fill_between(
        #         _squeeze.index, _squeeze, where=_squeeze > 0, 
        #         facecolor=verde_oscuro #'darkgreen'
        #     )
        # ax2.fill_between(
        #         _squeeze.index, _squeeze, where=(_squeeze > 0) & (_squeeze.shift() < _squeeze), 
        #         facecolor=verde_claro # Verde Claro.
        #     )
        # ax2.fill_between(
        #         _squeeze.index, _squeeze, where=_squeeze < 0, 
        #         facecolor=rojo_oscuro#'darkred'
        #     )
        # ax2.fill_between(
        #         _squeeze.index, _squeeze, where=(_squeeze < 0) & (_squeeze.shift() > _squeeze), 
        #         facecolor=rojo_claro#'red'
        #     )

        # ax[1].grid(linestyle='--', alpha=0.3)

        # Configuraciones finales       
        fig.suptitle(Titulo, color=contraste, alpha=0.7)
        fig.savefig(file)
        if show == True:
            plt.show()
        plt.close(fig)

    def plot_standard(
            self, 
            Graph_list,
            x,
            show = False,
        ):
        bot = info(
            self.pair,
            self.temporality,
        )

        df = bot.candlesticks()

        # Definiendo set de colores
        Titulo = f"Temporalidad {self.temporality}"
        sub_title1 = 'EMA10 y EMA55'
        sub_title2 = 'ADX y Squeeze Lazybear'
        Label_Graph1 = 'EMA10'
        Label_Graph2 = 'EMA55'
        Label_Graph3 = 'ADX'
        Label_Graph4 = 'Lazybear'
        LabelY = 'Price'
        file = 'plots/status.png'
        fondo = '#161A25'
        contraste = 'white'
        color_Graph1 = '#2962FF'
        color_Graph2 = '#FF6229'
        verde_claro = '#0A9711'
        verde_oscuro = '#0A5111'
        rojo_claro = '#AA1C20'
        rojo_oscuro = '#520B10'
        letras = '#9598A1'

        # Especificaciones generales de las graficas
        fig, ax = plt.subplots(2)
        # mpf.plot(df, ax = ax[0], ema = (10, 55), type='candle', style='charles', mavcolors = [color_Graph1, color_Graph2])
        fig.set_facecolor(fondo)

        # Graficando funcion 1
        # ax[0].set_ylabel(LabelY)
        # ax[0].set_facecolor(fondo) #fondo
        # ax[0].tick_params(colors=letras)
        # ax[0].yaxis.label.set_color(letras)
        # ax[0].xaxis.label.set_color(letras)


        # Graficando funcion 2
        # x = df.index.to_list()
        Graph = []
        for i in Graph_list:
            Graph.append([i for j in df.index.to_list()])

        for i in [0,1]:
            ax[0].plot(x, Graph[i], color=color_Graph1, label=Label_Graph2, alpha=0.3)

        ax[0].set_ylabel(LabelY)
        ax[0].set_facecolor(fondo) #fondo
        ax[0].tick_params(colors=letras)
        ax[0].yaxis.label.set_color(letras)
        ax[0].xaxis.label.set_color(letras)


        ax[0].grid(linestyle='--', alpha=0.3)

        # Configuraciones finales       
        fig.suptitle(Titulo, color=contraste, alpha=0.7)
        fig.savefig(file)
        if show == True:
            plt.show()
        plt.close(fig)