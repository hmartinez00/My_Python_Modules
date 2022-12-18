from MessagesKit.msgo import tg_msgo
from ManageDB.sqlite_on_db import *
import pandas as pd


class strmsgformat:

    def __init__(
        self,
        __table__,
        __date__,
        __title__,
        __Sub__,
        __text__,
    ):
        self.__table__ = __table__
        self.__date__ = __date__
        self.__title__ = __title__
        self.__Sub__ = __Sub__
        self.__text__ = __text__

    def msgtext(self):
        if self.__table__ == 'aguas_vivas_pasajes':
            send_pasaje = f"*{self.__title__}*\n" + f"*{self.__Sub__}*\n" + f"\n{self.__text__}"

        elif self.__table__ == 'aguas_vivas_comentarios':
            send_pasaje = f"*{self.__title__}*\n" + f"*{self.__Sub__}" + " _(Comentario:)_*\n" + f"\n{self.__text__}"
        
        elif self.__table__ == 'proverbios':
            send_pasaje = f"Preguntas sobre {self.__title__}\n\n" + f"{self.__text__}"

        elif self.__table__ == 'preguntas_la_buena_semilla':
            send_pasaje = f"Devocional del {self.__date__}\n\n" + f"{self.__Sub__}\n\n" + f"{self.__title__}\n\n" + f"Preguntas:\n\n{self.__text__}"

        elif self.__table__ == 'preguntas_la_buena_semilla':
            send_pasaje = f"Devocional del {self.__date__}\n\n" + f"{self.__Sub__}\n\n" + f"{self.__title__}\n\n" + f"Preguntas:\n\n{self.__text__}"

        elif self.__table__ == 'preguntas_lecturas':
            send_pasaje = f"Preguntas sobre: {self.__title__}\n\n" + f"{self.__text__}"

        else:
            print('''Error en modulo str_msg_format.py:

            El formato de mensaje para las entradas de esta tabla no se ha anadido!''')


        return send_pasaje


class buildmessage:

    def __init__(
        self,
        __database__,
        __table__,
        __Fecha__,
        __url__,
        __chat_id__,
        __token__,
    ):

        self.__database__ = __database__
        self.__table__ = __table__
        self.__Fecha__ = __Fecha__
        self.__url__ = __url__
        self.__chat_id__ = __chat_id__
        self.__token__ = __token__

    def sender(self):
        
        # Extraemos los datos de la base de datos
        df = selectall(self.__database__, self.__table__)
        df = df[df['Fecha'] == self.__Fecha__].reset_index()

        print(df)

        pregunta = input('Desea enviar en mensaje separados? (S/N): ')

        if pregunta == 's' or \
            pregunta == 'S':

            for i in range(len(df)):
                Tit = df['Titulo'][i]
                Sub = df['Subtitulo'][i]
                Tex = df['Texto'][i]

                # Construimos los mensajes
                send_pasaje = strmsgformat(
                        self.__table__,
                        self.__Fecha__,
                        Tit,
                        Sub,
                        Tex
                    ).msgtext()

                # Enviamos los mensajes
                tg_msgo(
                    self.__url__,
                    self.__chat_id__,
                    self.__token__,
                    send_pasaje,
                ).telegram_sender()
        
        elif pregunta == 'n' or pregunta == 'N':

            Tit = df['Titulo'][0]
            Sub = df['Subtitulo'][0]
            Tex = ''

            for i in range(len(df)):
                Tex = Tex + df['Texto'][i] + '\n'

            # Construimos los mensajes
            send_pasaje = strmsgformat(
                    self.__table__,
                    self.__Fecha__,
                    Tit,
                    Sub,
                    Tex
                ).msgtext()

            # Enviamos los mensajes
            tg_msgo(
                self.__url__,
                self.__chat_id__,
                self.__token__,
                send_pasaje,
            ).telegram_sender()
        
        else:
            print('Opcion invalida!')