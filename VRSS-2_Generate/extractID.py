# ---------------------------------------------------------------------
# ABAE-SAT-UT-SGO
# Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
# Creación: 2022-08-19
# Actualización: 2022-08-19
#
#   Script para generación del CPLAN2.
#
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Importamos las librerías.
# ---------------------------------------------------------------------
import os
import pandas as pd
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

from on_db import *
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# Funcion de extraccion de IDs.
# ---------------------------------------------------------------------
def extractid(__var_archivo__):

    __values__ = {}

    __xml_data__ = open(__var_archivo__, 'r').read()
    __root__ = ET.XML(__xml_data__)

    for i, __child__0 in enumerate(__root__):

        for __child__1 in __child__0:
            if __child__1.tag.find('MessageID') == 0 or \
                __child__1.tag.find('MessageType') == 0 or \
                __child__1.tag.find('Originator') == 0 or \
                __child__1.tag.find('Recipient') == 0 or \
                __child__1.tag.find('MessageCreateTime') == 0:                
                __values__[__child__1.tag] = __child__1.text

            for __child__2 in __child__1:                        
                for __child__3 in __child__2:                    
                    for __child__4 in __child__3:
                        for __child__5 in __child__4:
                            for __child__6 in __child__5:
                                for __child__7 in __child__6:
                                    for __child__8 in __child__7:
                                        for __child__9 in __child__8:
                                            continue

    return __values__

# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# Actualizacion de tabla de control de procesos
# ---------------------------------------------------------------------
def IDUpdate(__fecha__):

    S_base_datos = 'vrss_operation_and_managment_subsystem'
    S_tabla = '`control_misiones_id_control_process`'

    sub_directorio = 'Plan Satelital ' + str(__fecha__) + '/'
#     os.chdir('..')
#     os.chdir('backup/PMS/' + sub_directorio)
    os.chdir(sub_directorio)
    directorio = os.getcwd()

    rutas = []

    for nombre_directorio, dirs, ficheros in os.walk(directorio):
        for nombre_fichero in ficheros:
            if '.CPLAN' in nombre_fichero or \
                '.SETPARA' in nombre_fichero or \
                '.OK' in nombre_fichero or \
                '.RECEIVETASK' in nombre_fichero :
                ruta = nombre_directorio + '\\' + nombre_fichero
                rutas.append(ruta.replace('\\', '/'))

    dt = []
    for i in range(len(rutas)):
        dt.append(pd.DataFrame(extractid(rutas[i]), index=[i]))
    
    df = pd.concat(dt)#.reset_index()

    df = df.sort_values('MessageCreateTime')

    df['Index'] = [i for i in range(len(df))]

    df.set_index('Index',inplace=True)
    df.index.name = None

    epoch_format = []
    for i in range(len(df)):
        epoch_format.append(
        datetime.strftime(
            datetime.strptime(
            df['MessageCreateTime'][i]
                , '%Y-%m-%dT%H:%M:%S'
            ), '%Y-%m-%d %H:%M:%S'
        ))

    df['MessageCreateTime'] = epoch_format
    df['MessageCreateTime'] = pd.to_datetime(df['MessageCreateTime'])

    Insertar_registro_masivo(df, S_base_datos, S_tabla)
     
# ---------------------------------------------------------------------