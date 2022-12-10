# ---------------------------------------------------------------------
# ABAE-SAT-UT-SGO
# Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
# Actualización: 2022-08-12
#
#   Módulo para la actualización de la tabla:
#   "control_misiones_instantaneous_data_info"
#
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Importamos las librerías.
# ---------------------------------------------------------------------
from datetime import datetime
import xml.etree.ElementTree as ET

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Extracción de datos de los XML.
# ---------------------------------------------------------------------
def EPH_extract(__var_archivo__):

    __values__ = {}

    __xml_data__ = open(__var_archivo__, 'r').read()
    __root__ = ET.XML(__xml_data__)

    for i, __child__0 in enumerate(__root__):

        __values__['OrbitID'] = ''

        for __child__1 in __child__0:
            if __child__1.tag.find('MessageID') == 0 or \
                __child__1.tag.find('MessageType') == 0 or \
                __child__1.tag.find('Originator') == 0 or \
                __child__1.tag.find('Recipient') == 0 or \
                __child__1.tag.find('MessageCreateTime') == 0 or \
                __child__1.tag.find('DataID') == 0 or \
                __child__1.tag.find('SatelliteID') == 0 or \
                __child__1.tag.find('OrbitID') == 0 or \
                __child__1.tag.find('OrbitEpoch') == 0 or \
                __child__1.tag.find('OrbitRadius') == 0 or \
                __child__1.tag.find('OrbitPartialityRatio') == 0 or \
                __child__1.tag.find('OrbitObliquity') == 0 or \
                __child__1.tag.find('AscendPoint') == 0 or \
                __child__1.tag.find('NearPointAngle') == 0 or \
                __child__1.tag.find('BreadthAngle') == 0:
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

    __values__['EPHFileName'] = \
        __values__['Originator'] + '_' + \
        __values__['Recipient'] + '_' + \
        __values__['SatelliteID'] + '_' + \
        str(datetime.strftime(
        datetime.strptime(
        __values__['MessageCreateTime']
            , '%Y-%m-%dT%H:%M:%S'
        ), '%Y%m%d')) + '_' + \
        __values__['MessageID'] + '.' + \
        __values__['MessageType']

    return __values__

# ---------------------------------------------------------------------