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
            send_pasaje = f"Preguntas sobre {self.__title__}\n\n" + f"{self.__Sub__}\n\nPreguntas:\n\n" + f"{self.__text__}"

        elif self.__table__ == 'preguntas_la_buena_semilla':
            send_pasaje = f"Devocional del {self.__date__}\n\n" + f"{self.__Sub__}\n\n" + f"{self.__title__}\n\n" + f"Preguntas:\n\n{self.__text__}"

        elif self.__table__ == 'preguntas_lecturas':
            send_pasaje = f"Preguntas sobre: {self.__title__}\n\n" + f"{self.__Sub__}\n\n" + f"{self.__text__}"

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


class strTmsgformat:

    def __init__(
        self,
        __table__,
        __date__,
        __Lista__,
    ):
        self.__table__ = __table__
        self.__date__ = __date__
        self.__Lista__ = __Lista__

    def msgtext(self):
        if self.__table__ == 'plan_biblia_52':
            send_pasaje_0 = \
            f"Lectura del {self.__date__}:  " + \
            f"{self.__Lista__[0]}\n\n"

            if self.__Lista__[1] != '' and 'Panorama' not in self.__Lista__[1]:
                send_pasaje_0 = send_pasaje_0 + \
                f"Bosquejo - {self.__Lista__[1]}\n" + \
                f"Conteste las siguientes preguntas:\n\n" + \
                f"1. Cuantos capítulos tiene el libro?\n" + \
                f"2. En cuantas partes se divide el libro y cuales son?\n" + \
                f"3. De qué trata cada parte del libro mostrada en el video?\n" + \
                f"4. Enumere 3 enseñanzas correspondientes a cada una de las partes del libro mostradas en el video.\n\n" + \
                f"{self.__Lista__[2]}"

            elif self.__Lista__[1] != '' and 'Panorama' in self.__Lista__[1]:
                send_pasaje_0 = send_pasaje_0 + \
                f"{self.__Lista__[1]}\n\n" + \
                f"{self.__Lista__[2]}"

            
            if self.__Lista__[3] != '':
                send_pasaje_1 = \
                f"Trivia Biblica:\n\n" + \
                f"Instrucciones:\n\n" + \
                f"1. Una vez entre al link contara con 30min para responder a las preguntas.\n" + \
                f"2. Si culmina antes del tiempo presiones enviar. Sus resultados apareceran en un recuadro en la parte superior de la pagina.\n" + \
                f"3. Si el tiempo se agota la pagina se congelará y sus resultados apareceran en un recuadro en la parte superior de la pagina.\n" + \
                f"4. En cualquiera de ambos casos, al finalizar, tome un screenshot de sus resultados y envielas al grupo.\n\n" + \
                f"Que el Espíritu Santo le guíe a toda verdad.\n\n" + \
                f"{self.__Lista__[3]}"
            
            elif self.__Lista__[3] == '':
                send_pasaje_1 = ''


        else:
            print('''Error en modulo str_msg_format.py:

            El formato de mensaje para las entradas de esta tabla no se ha anadido!''')


        send_pasaje = [send_pasaje_0, send_pasaje_1]

        return send_pasaje


class build_Tmsg:

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

    def sender(self, __Lista__):
        
        N_lista = []

        # Extraemos los datos de la base de datos
        df = selectall(self.__database__, self.__table__)
        df = df[df['Fecha'] == self.__Fecha__].reset_index()

        for i in range(len(__Lista__)):
            entry = df[__Lista__[i]].iloc[0]
            print(entry)
            N_lista.append(entry)

        # Construimos los mensajes
        send_pasaje = strTmsgformat(
                self.__table__,
                self.__Fecha__,
                N_lista
            ).msgtext()

        print(send_pasaje)

        # Enviamos los mensajes
        tg_msgo(
            self.__url__,
            self.__chat_id__,
            self.__token__,
            send_pasaje[0],
        ).telegram_sender()

        if send_pasaje[1] != '':
            tg_msgo(
                self.__url__,
                self.__chat_id__,
                self.__token__,
                send_pasaje[1],
            ).telegram_sender()