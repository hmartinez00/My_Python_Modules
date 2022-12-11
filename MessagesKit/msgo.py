import requests
import msg_config as cfg
from datetime import datetime, timedelta

import pywhatkit
# import time
# import webbrowser as web
# from urllib.parse import quote
# import pyautogui as pg
# from pywhatkit.core import core, exceptions, log


class tg_msgo:

    def __init__(
            self,
            __chat_id__,
            __token__,
            __message__,
        ):

        self.__chat_id__ = __chat_id__
        self.__token__ = __token__
        self.__message__ = __message__

    def telegram_sender(self):
        '''
        Enviara el mensaje almacenado en self.message, a traves del bot de telegram.
        '''
        __telegram_url__ = cfg.TELEGRAM_URL

        requests.post(__telegram_url__ + self.__token__ + '/sendMessage',
                data={'chat_id': self.__chat_id__, 'text': self.__message__})

class ws_msgo:

    def __init__(
            self,
            __phone__,
            __message__,
        ):

        ahora = datetime.now()
        delay = ahora + timedelta(minutes=1)
    
        self.__phone__ = __phone__
        self.__message__ = __message__
        self.wait_time = 10
        # self.hour = delay.hour
        # self.min = delay.minute

    
    def whatsapp_sender(self):
        '''
        Enviara el mensaje almacenado en self.message, al minuto siguiente del envio a traves de una api de whatsapp.
        '''

        pywhatkit.sendwhatmsg_instantly(
                self.__phone__, 
                self.__message__,
                self.wait_time,
                # self.hour, 
                # self.min
            )

        # pg.FAILSAFE = False
        # core.check_connection()
        
        # web.open(f"https://web.whatsapp.com/send?phone={self.__phone__}&text={quote(self.__message__)}")
        # time.sleep(4)
        # pg.click(core.WIDTH / 2, core.HEIGHT / 2)
        # time.sleep(self.wait_time - 4)
        # pg.press("enter")