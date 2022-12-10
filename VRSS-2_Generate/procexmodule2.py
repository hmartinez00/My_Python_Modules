import os
import pandas as pd
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

from prettify import prettify

def inspect_XML(var_archivo):

    xml_data = open(var_archivo, 'r').read()
    root = ET.XML(xml_data)

    for i, child0 in enumerate(root):
        print('{} '.format(0), child0.tag + ':', child0.text, '\t' + str(len(child0)))
        for child1 in child0:
            print('\t{} '.format(1), child1.tag + ':', child1.text, '\t' + str(len(child1)))
            for child2 in child1:
                print('\t\t{} '.format(2), child2.tag + ':', child2.text, '\t' + str(len(child2)))
                for child3 in child2:
                    print('\t\t\t{} '.format(3), child3.tag + ':', child3.text, '\t' + str(len(child3)))
                    for child4 in child3:
                        print('\t\t\t\t{} '.format(4), child4.tag + ':', child4.text, '\t' + str(len(child4)))
                        for child5 in child4:
                            print('\t\t\t\t\t{} '.format(5), child5.tag + ':', child5.text, '\t' + str(len(child5)))
                            for child6 in child5:
                                print('\t\t\t\t\t\t{} '.format(6), child6.tag + ':', child6.text, '\t' + str(len(child6)))
                                for child7 in child6:
                                    print('\t\t\t\t\t\t\t{} '.format(7), child7.tag + ':', child7.text, '\t' + str(len(child7)))
                                    for child8 in child7:
                                        print('\t\t\t\t\t\t\t\t{} '.format(8), child8.tag + ':', child8.text, '\t' + str(len(child8)))
                                        for child9 in child8:
                                            print('\t\t\t\t\t\t\t\t\t{} '.format(9), child9.tag + ':', child9.text, '\t' + str(len(child9)))


def CPLAN_extract(__var_archivo__):

    __values__ = {}

    __xml_data__ = open(__var_archivo__, 'r').read()
    __root__ = ET.XML(__xml_data__)

    for i, __child__0 in enumerate(__root__):

        for __child__1 in __child__0:
            if __child__1.tag.find('MessageID') == 0 or \
                __child__1.tag.find('MessageType') == 0 or \
                __child__1.tag.find('Originator') == 0 or \
                __child__1.tag.find('Recipient') == 0 or \
                __child__1.tag.find('MessageCreateTime') == 0 or \
                __child__1.tag.find('TaskID') == 0 or \
                __child__1.tag.find('FirstOrbitTime') == 0:
                __values__[__child__1.tag] = __child__1.text

            for __child__2 in __child__1:
                if __child__2.tag.find('PlanID') == 0 or \
                    __child__2.tag.find('SatelliteID') == 0 or \
                    __child__2.tag.find('WorkMode') == 0 or \
                    __child__2.tag.find('OrbitID') == 0 or \
                    __child__2.tag.find('TransStartTime') == 0 or \
                    __child__2.tag.find('TransEndTime') == 0 or \
                    __child__2.tag.find('ReplayFile') == 0 or \
                    __child__2.tag.find('DeleteFile') == 0 or \
                    __child__2.tag.find('ImagingCount') == 0:
                    if __child__2.tag in __values__.keys():
                        __values__[__child__2.tag].append(__child__2.text)
                    else:
                        __values__[__child__2.tag] = [__child__2.text]
                        
                for __child__3 in __child__2:
                    if __child__3.tag.find('ImagingID') == 0 or \
                        __child__3.tag.find('RollAngle') == 0 or \
                        __child__3.tag.find('FileName') == 0 or \
                        __child__3.tag.find('ImageStartTime') == 0 or \
                        __child__3.tag.find('ImageEndTime') == 0:
                        if __child__3.tag in __values__.keys():
                            __values__[__child__3.tag].append(__child__3.text)
                        else:
                            __values__[__child__3.tag] = [__child__3.text]
                    
                    for __child__4 in __child__3:
                        for __child__5 in __child__4:
                            for __child__6 in __child__5:
                                for __child__7 in __child__6:
                                    for __child__8 in __child__7:
                                        for __child__9 in __child__8:
                                            continue

    __values__['PlanFileName'] = \
        __values__['Originator'] + '_' + \
        __values__['Recipient'] + '_' + \
        __values__['SatelliteID'][0] + '_' + \
        str(datetime.strftime(
        datetime.strptime(
        __values__['MessageCreateTime']
            , '%Y-%m-%dT%H:%M:%S'
        ), '%Y%m%d')) + '_' + \
        __values__['MessageID'] + '.' + \
        __values__['MessageType']

    return __values__


def TCPLAN_extract(__var_archivo__):

    __values__ = {}

    __xml_data__ = open(__var_archivo__, 'r').read()
    __root__ = ET.XML(__xml_data__)

    for i, __child__0 in enumerate(__root__):
        if __child__0.tag.find('MadeTime') == 0 or \
            __child__0.tag.find('FileTS') == 0 or \
            __child__0.tag.find('FileTE') == 0:
            if __child__0.tag in __values__.keys():
                __values__[__child__0.tag].append(__child__0.text)
            else:
                __values__[__child__0.tag] = [__child__0.text]

        for __child__1 in __child__0:
            for __child__2 in __child__1:
                if __child__2.tag.find('SCNAME') == 0 or \
                    __child__2.tag.find('DEVNAME') == 0 or \
                    __child__2.tag.find('REVNUM') == 0 or \
                    __child__2.tag.find('MAXE') == 0 or \
                    __child__2.tag.find('TTS') == 0 or \
                    __child__2.tag.find('TTE') == 0 or \
                    __child__2.tag.find('TTSL') == 0 or \
                    __child__2.tag.find('TTEL') == 0:
                    if __child__2.tag in __values__.keys():
                        __values__[__child__2.tag].append(__child__2.text)
                    else:
                        __values__[__child__2.tag] = [__child__2.text]
                        
                for __child__3 in __child__2:                    
                    for __child__4 in __child__3:
                        for __child__5 in __child__4:
                            for __child__6 in __child__5:
                                for __child__7 in __child__6:
                                    for __child__8 in __child__7:
                                        for __child__9 in __child__8:
                                            continue

    __values__['MadeTime'] = [__values__['MadeTime'][0] for i in __values__['SCNAME']]
    __values__['FileTS'] = [__values__['FileTS'][0] for i in __values__['SCNAME']]
    __values__['FileTE'] = [__values__['FileTE'][0] for i in __values__['SCNAME']]

    return __values__



def secuencia(__CPLAN_extract__):

# 1. Creamos el diccionario de almacenamiento de valores.
    __secuencia__ = {}
        
# 2. Determinamos el numero de tomas programadas y sus PlanID.
    __secuencia__['PlanID'] = []
    for i in range(len(__CPLAN_extract__['ImageStartTime'])):
        if __CPLAN_extract__['ImageStartTime'][i] != None:
            __secuencia__['PlanID'].append(__CPLAN_extract__['PlanID'][i])

    __secuencia__['TransStartTime'] = []
    for i in range(len(__CPLAN_extract__['TransStartTime'])):
        if __CPLAN_extract__['TransStartTime'][i] != None:
            __secuencia__['TransStartTime'].append(__CPLAN_extract__['TransStartTime'][i])
            
    __secuencia__['TransEndTime'] = []
    for i in range(len(__CPLAN_extract__['TransEndTime'])):
        if __CPLAN_extract__['TransEndTime'][i] != None:
            __secuencia__['TransEndTime'].append(__CPLAN_extract__['TransEndTime'][i])

    __secuencia__['OrbitID'] = []
    for i in range(len(__CPLAN_extract__['TransEndTime'])):
        if __CPLAN_extract__['TransEndTime'][i] != None:
            __secuencia__['OrbitID'].append(__CPLAN_extract__['OrbitID'][i])

# 3. Definimos las ID de los parametros de camara.   
    __secuencia__['ParameterID'] = []
    for i in range(len(__secuencia__['PlanID'])):
        __secuencia__['ParameterID'].append( \
        str(int(__secuencia__['PlanID'][0]) + i) \
        )

# 4. Calculamos el numero de archivos que deben ser generados.este debe corresponder
# con el numero de pasos que deberia ejecutar el proceso de generacion.
    __steps__ = 2 * len(__secuencia__['PlanID']) + 1
    
# 5. Definimos los tiempos de creacion de cada archivo.
    __MessageCreateTime__0 = __CPLAN_extract__['MessageCreateTime']
    __MessageCreateTime__1 = datetime.strptime(__MessageCreateTime__0, '%Y-%m-%dT%H:%M:%S')
    __secuencia__['MessageCreateTime'] = []
    for i in range(__steps__):        
        if i <= len(__secuencia__['PlanID']):
            __timedelta__ = timedelta(seconds=2*i+2)
        else:
            __timedelta__ = timedelta(minutes=5, seconds=i)
        __secuencia__['MessageCreateTime'].append(    
            datetime.strftime(__MessageCreateTime__1 + __timedelta__, '%Y-%m-%dT%H:%M:%S')
        )

# 7. Definimos los ID de cada archivo a generar
    __secuencia__['MessageID'] = []
    for i in range(len(__secuencia__['MessageCreateTime'])):
        __secuencia__['MessageID'].append( \
        str(int(__CPLAN_extract__['MessageID']) + i + 2).rjust(12, '0') \
        )

    __secuencia__['ReplayWorkmode'] = []
    for i in range(len(__CPLAN_extract__['TransStartTime'])):
        if __CPLAN_extract__['TransStartTime'][i] != None and \
            __CPLAN_extract__['ImageStartTime'][i] != None:
            __secuencia__['ReplayWorkmode'].append('1')
        elif __CPLAN_extract__['TransStartTime'][i] != None and \
            __CPLAN_extract__['ImageStartTime'][i] == None:
            __secuencia__['ReplayWorkmode'].append('2')
        else:
            continue
    

    return __secuencia__


def SETPARAS_builder(__CPLAN_extract__):

    secuencia(__CPLAN_extract__)

    __SETPARAS_values__ = {}
    __limit__0 = len(secuencia(__CPLAN_extract__)['MessageID'])
    __limit__ = (__limit__0 - 1) / 2 - 1

    __limit_PlanID__ = len(secuencia(__CPLAN_extract__)['PlanID'])

    __SETPARAS_values__['MessageID'] = []
    for i in range(__limit__0):
        if i <= __limit__:
          __SETPARAS_values__['MessageID'].append( \
               str(secuencia(__CPLAN_extract__)['MessageID'][i]) \
               )

    __SETPARAS_values__['MessageType'] = ['SETPARA2' \
     for i in range(__limit_PlanID__)]
    __SETPARAS_values__['Originator'] = [__CPLAN_extract__['Originator'] \
     for i in range(__limit_PlanID__)]
    __SETPARAS_values__['Recipient'] = [__CPLAN_extract__['Recipient'] \
     for i in range(__limit_PlanID__)]

    __SETPARAS_values__['MessageCreateTime'] = []
    for i in range(__limit__0):
        if i <= __limit__:
          __SETPARAS_values__['MessageCreateTime'].append( \
               str(secuencia(__CPLAN_extract__)['MessageCreateTime'][i]) \
          )      

    __SETPARAS_values__['TaskID'] = [__CPLAN_extract__['TaskID'] \
         for i in range(__limit_PlanID__)]

    __SETPARAS_values__['ParameterID'] = []
    for i in range(len(secuencia(__CPLAN_extract__)['ParameterID'])):
        __SETPARAS_values__['ParameterID'].append( \
          str(secuencia(__CPLAN_extract__)['ParameterID'][i]) \
          )

    __SETPARAS_values__['SatelliteID'] = [__CPLAN_extract__['SatelliteID'][0] \
         for i in range(__limit_PlanID__)]

    __SETPARAS_values__['PlanID'] = []
    for i in range(__limit_PlanID__):
        __SETPARAS_values__['PlanID'].append( \
          str(secuencia(__CPLAN_extract__)['PlanID'][i]) \
          )

    __SETPARAS_values__['ImagingID'] = ['0001' for i in range(__limit_PlanID__)]  
    __SETPARAS_values__['CompressRatio'] = ['1206AAAAH' for i in range(__limit_PlanID__)]  
    __SETPARAS_values__['HRC_Gain_P'] = ['06H' for i in range(__limit_PlanID__)] 
    __SETPARAS_values__['HRC_Gain_B1'] = ['06H' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['HRC_Gain_B2'] = ['0AH' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['HRC_Gain_B3'] = ['06H' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['HRC_Gain_B4'] = ['08H' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['HRC_TDI_P'] = ['03H' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['HRC_TDI_B1'] = ['04H' for i in range(__limit_PlanID__)] 
    __SETPARAS_values__['HRC_TDI_B2'] = ['03H' for i in range(__limit_PlanID__)] 
    __SETPARAS_values__['HRC_TDI_B3'] = ['04H' for i in range(__limit_PlanID__)] 
    __SETPARAS_values__['HRC_TDI_B4'] = ['03H' for i in range(__limit_PlanID__)] 
    __SETPARAS_values__['IRC_Gain_B1'] = ['00H' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['IRC_Gain_B2'] = ['08H' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['IRC_Gain_B3'] = ['04H' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['IRC_Gain_B4'] = ['03H' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['IRC_Gain_B5'] = ['03H' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['IRC_Time_B1'] = ['0A8CH' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['IRC_Time_B2'] = ['0A8CH' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['IRC_Time_B3'] = ['0A8CH' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['IRC_Time_B4'] = ['0064H' for i in range(__limit_PlanID__)]
    __SETPARAS_values__['IRC_Time_B5'] = ['0064H' for i in range(__limit_PlanID__)]  
    
    
    __SETPARAS_values__['ParameterFileName'] = []
    for i in range(__limit_PlanID__):
        __Originator__ = __SETPARAS_values__['Originator'][i]
        __Recipient__ = __SETPARAS_values__['Recipient'][i]
        __SatelliteID__ = __SETPARAS_values__['SatelliteID'][i]
        __PlanID__ = __SETPARAS_values__['PlanID'][i]
        __ImagingID__ = __SETPARAS_values__['ImagingID'][i]
        __MessageType__ = __SETPARAS_values__['MessageType'][i]
        __SETPARAS_values__['ParameterFileName'].append(
            __Originator__ + '_' + \
            __Recipient__ + '_' + \
            __SatelliteID__ + '_' + \
            __PlanID__ + '_' + \
            __ImagingID__ + '.' + \
            __MessageType__
        )

    return __SETPARAS_values__
     
     
def OK_builder(__CPLAN_extract__):

    secuencia(__CPLAN_extract__)
     
    __OK_Values__ = {}

    __limit__0 = len(secuencia(__CPLAN_extract__)['MessageID'])
    __limit__ = (__limit__0 - 1) / 2

    __OK_Values__['MessageID'] = secuencia(__CPLAN_extract__)['MessageID'][int(__limit__)]
    __OK_Values__['MessageType'] = 'OK'
    __OK_Values__['Originator'] = __CPLAN_extract__['Originator']
    __OK_Values__['Recipient'] = __CPLAN_extract__['Recipient']
    __OK_Values__['MessageCreateTime'] = secuencia(__CPLAN_extract__)['MessageCreateTime'][int(__limit__)]
    __OK_Values__['TaskID'] = __CPLAN_extract__['TaskID']
    
    __OK_Values__['StartNotifyID'] = str(int(datetime.strftime(
          datetime.strptime(
          __CPLAN_extract__['FirstOrbitTime']
               , '%Y-%m-%dT%H:%M:%S'
          ), '%Y%m%d'
     )
    ) * 1000000 + 3)

    __OK_Values__['PlanFileName'] =  __CPLAN_extract__['PlanFileName']

    __OK_Values__['FocusFileName'] = ' '

    __SETPARAS_builder__ = SETPARAS_builder(__CPLAN_extract__)

    __OK_Values__['ParameterFileCount'] = str(len(__SETPARAS_builder__['ParameterFileName']))

    __OK_Values__['ParameterFileName'] = [
        __SETPARAS_builder__['ParameterFileName'][i] \
        for i in range(len(__SETPARAS_builder__['ParameterFileName']))
    ]

    __OK_Values__['OKFileName'] = \
        __CPLAN_extract__['Originator'] + '_' + \
        __CPLAN_extract__['Recipient'] + '_' + \
        __CPLAN_extract__['SatelliteID'][0] + '_' + \
        str(datetime.strftime(
        datetime.strptime(
        __CPLAN_extract__['MessageCreateTime']
            , '%Y-%m-%dT%H:%M:%S'
        ), '%Y%m%d')) + '_' + \
        __OK_Values__['MessageID'] + '.' + \
        __OK_Values__['MessageType']
    

    return __OK_Values__


def near_orbits(__CPLAN_extract__, __RecPass__):

    __Enganche__ = secuencia(__CPLAN_extract__)['TransStartTime']
    __delay_min__ = []
    __CaptureTime__0 = []
    __near_orbits_dict__ = {}

    for j in range(len(__Enganche__)):

        __orbitas_cercanas__ = []

        __fecha_hora__ = datetime.strptime(
            __Enganche__[j]
            , '%Y-%m-%dT%H:%M:%S'
        )

        __RecPass__['Diff'] = __fecha_hora__ - __RecPass__['CaptureStartTime']

        for i in range(len(__RecPass__['Diff'])):
            if int(__RecPass__['Diff'].dt.days[i]) == 0:
                __orbitas_cercanas__.append(__RecPass__['Diff'][i])

        __delay_min__.append(pd.Series(__orbitas_cercanas__).min())

        __CaptureTime__0.append(__RecPass__[__RecPass__['Diff'] == __delay_min__[j]])
        __CaptureTime__ = pd.concat(__CaptureTime__0).reset_index()
        
        __near_orbits_dict__['CaptureStartTime'] = []
        __near_orbits_dict__['CaptureEndTime'] = []
        for i in range(len(__CaptureTime__)):
            __near_orbits_dict__['CaptureStartTime'].append(
                datetime.strftime(
                    __CaptureTime__.iloc[i]['CaptureStartTime']
                    , '%Y-%m-%dT%H:%M:%S'
                ))
            __near_orbits_dict__['CaptureEndTime'].append(
                datetime.strftime(
                    __CaptureTime__.iloc[i]['CaptureEndTime']
                    , '%Y-%m-%dT%H:%M:%S'
                ))

    return __near_orbits_dict__


def RECEIVETASK_builder(__CPLAN_extract__, __RecPass__):
    
    __secuencia_dict__ = secuencia(__CPLAN_extract__)
    __CaptureTime_dict__ = near_orbits(__CPLAN_extract__, __RecPass__)

    __RECEIVETASK_values__ = {}
    __limit__0 = len(__secuencia_dict__['MessageID'])
    __limit__ = (__limit__0 - 1) / 2

    __limit_PlanID__ = len(__secuencia_dict__['PlanID'])

    __RECEIVETASK_values__['MessageID'] = []
    for i in range(__limit__0):
        if i > __limit__:
          __RECEIVETASK_values__['MessageID'].append( \
               str(__secuencia_dict__['MessageID'][i]) \
               )
    __RECEIVETASK_values__['MessageType'] = ['RECEIVETASK' \
     for i in range(__limit_PlanID__)]
    __RECEIVETASK_values__['Originator'] = [__CPLAN_extract__['Originator'] \
     for i in range(__limit_PlanID__)]
    __RECEIVETASK_values__['Recipient'] = ['TDRS' \
     for i in range(__limit_PlanID__)]

    __RECEIVETASK_values__['MessageCreateTime'] = []
    for i in range(__limit__0):
        if i > __limit__:
          __RECEIVETASK_values__['MessageCreateTime'].append( \
               str(__secuencia_dict__['MessageCreateTime'][i]) \
          )

    __RECEIVETASK_values__['TaskID'] = [str(int(
               __CPLAN_extract__['TaskID'][:8] + '01' + \
               __CPLAN_extract__['TaskID'][8:]
          ) + i + 1) \
         for i in range(__limit_PlanID__)]

    __RECEIVETASK_values__['OrderID'] = [str(int(datetime.strftime(
          datetime.strptime(
          __CPLAN_extract__['MessageCreateTime']
               , '%Y-%m-%dT%H:%M:%S'
          ), '%Y%m%d'
     ) + '01'
    ) * 1000000 + 25 + i) for i in range(__limit_PlanID__)]

    __RECEIVETASK_values__['OperatorName'] = ['AUTOMATION' \
     for i in range(__limit_PlanID__)]
     # str(CaptureStartTime[i])
    __RECEIVETASK_values__['CaptureStartTime'] = [ \
         __CaptureTime_dict__['CaptureStartTime'][i] \
     for i in range(__limit_PlanID__)]
    __RECEIVETASK_values__['CaptureEndTime'] = [ \
         __CaptureTime_dict__['CaptureEndTime'][i] \
     for i in range(__limit_PlanID__)]

    __RECEIVETASK_values__['StartReceiveTime'] = [ \
         str(__secuencia_dict__['TransStartTime'][i]) \
     for i in range(__limit_PlanID__)]
    __RECEIVETASK_values__['EndReceiveTime'] = [ \
         str(__secuencia_dict__['TransEndTime'][i]) \
     for i in range(__limit_PlanID__)]

    __RECEIVETASK_values__['SatelliteID'] = ['VRSS-2' \
     for i in range(__limit_PlanID__)]
    __RECEIVETASK_values__['StationID'] = ['FGS-1' \
     for i in range(__limit_PlanID__)]
    __RECEIVETASK_values__['SensorID'] = ['IRC,HRC' \
     for i in range(__limit_PlanID__)]
    __RECEIVETASK_values__['ChannelNum'] = ['CH1,CH2' \
     for i in range(__limit_PlanID__)]
    __RECEIVETASK_values__['OrbitID'] = [ \
         str(__secuencia_dict__['OrbitID'][i]) \
     for i in range(__limit_PlanID__)]
    __RECEIVETASK_values__['WorkMode'] = __secuencia_dict__['ReplayWorkmode']
    __RECEIVETASK_values__['TranslateMode'] = ['2' \
     for i in range(__limit_PlanID__)]


    __RECEIVETASK_values__['ReceiveFileName'] = []
    for i in range(__limit_PlanID__):
        __Originator__ = __RECEIVETASK_values__['Originator'][i]
        __Recipient__ = __RECEIVETASK_values__['Recipient'][i]
        __SatelliteID__ = __RECEIVETASK_values__['SatelliteID'][i]
        __BatchID__ = str(datetime.strftime(
               datetime.strptime(
               __RECEIVETASK_values__['MessageCreateTime'][i]
                    , '%Y-%m-%dT%H:%M:%S'
               ), '%Y%m%d'))
        __MessageID__ = __RECEIVETASK_values__['MessageID'][i]
        __MessageType__ = __RECEIVETASK_values__['MessageType'][i]
        __RECEIVETASK_values__['ReceiveFileName'].append(
            __Originator__ + '_' + \
            __Recipient__ + '_' + \
            __SatelliteID__ + '_' + \
            __BatchID__ + '_' + \
            __MessageID__ + '.' + \
            __MessageType__
        )

    return __RECEIVETASK_values__


def directories_builder(__CPLAN_extract__):

    __directories__ = {}

    BatchID = str(datetime.strftime(
        datetime.strptime(__CPLAN_extract__['FirstOrbitTime'], 
        '%Y-%m-%dT%H:%M:%S'), '%Y%m%d'))
     
    root = 'Plan Satelital ' + BatchID + '/'
    satellite_Plan = root + 'VRSS-2'
    station_Plan = root + 'Station Plan'

    __directories__['root'] = root
    __directories__['satellite_Plan'] = satellite_Plan
    __directories__['station_Plan'] = station_Plan

    return __directories__


def directories_generator(__directories_path__):

    try:
        os.makedirs(__directories_path__['satellite_Plan'])
        os.makedirs(__directories_path__['station_Plan'])
    except:
        return 'El directorio ya existe!'
    
    
def XML_SETPARA_Generator(__SETPARA_dict__, __ParameterFileCount__):

    __ParameterFileName__ = __SETPARA_dict__['ParameterFileName'][__ParameterFileCount__]
    __SETPARA_Keys__ = []
    __SETPARA_Valores__ = []

    [__SETPARA_Keys__.append(i) for i in __SETPARA_dict__.keys()]
    [__SETPARA_Valores__.append(__SETPARA_dict__[__SETPARA_Keys__[i]][__ParameterFileCount__]) for i in range(len(__SETPARA_Keys__))]

    SETPARA = Element('SETPARA')

    __FileHeader__ = SubElement(SETPARA, 'FileHeader')
    __FileBody__ = SubElement(SETPARA, 'FileBody')

    for i in range(len(__SETPARA_Keys__)):
        if i <= 4:
            __fild__ = __SETPARA_Keys__[i]
            __fild__ = SubElement(__FileHeader__, __fild__)
            __fild__.text = __SETPARA_Valores__[i]

        if i > 4 and i < len(__SETPARA_Keys__) - 1:
            __fild__ = __SETPARA_Keys__[i]
            __fild__ = SubElement(__FileBody__, __fild__)
            __fild__.text = __SETPARA_Valores__[i]

    __cadena__0 = prettify(SETPARA)
    __cadena__ = __cadena__0.replace('<?xml version="1.0" ?>', '<?xml version="1.0" encoding="utf-8"?>')
    f = open(__ParameterFileName__, 'w')
    f.write(__cadena__)
    f.close()
    
    
def XML_OK_generator(__OK_dict__):
     
    __OK_Keys__ = []
    __OK_Valores__ = []

    [__OK_Keys__.append(i) for i in __OK_dict__.keys()]
    [__OK_Valores__.append(__OK_dict__[__OK_Keys__[i]]) for i in range(len(__OK_Keys__))]

    __OKFileName__ = __OK_dict__['OKFileName']

    OK = Element('OK')

    __FileHeader__ = SubElement(OK, 'FileHeader')
    __FileBody__ = SubElement(OK, 'FileBody')

    for i in range(len(__OK_Keys__) + 1):
        if i <= 4:
            __fild__ = __OK_Keys__[i]
            __fild__ = SubElement(__FileHeader__, __fild__)
            __fild__.text = __OK_Valores__[i]
            
        if i > 4 and i < len(__OK_Keys__) - 2:
            __fild__ = __OK_Keys__[i]
            __fild__ = SubElement(__FileBody__, __fild__)
            __fild__.text = __OK_Valores__[i]
        
        if i == len(__OK_Keys__) - 1:
            for j in range(len(__OK_dict__['ParameterFileName'])):
                __FileList__ = SubElement(__FileBody__, 'FileList')
                __ParameterFileName__ = SubElement(__FileList__, 'ParameterFileName')
                __ParameterFileName__.text = __OK_dict__['ParameterFileName'][j]

    __cadena__0 = prettify(OK)
    __cadena__ = __cadena__0.replace('<?xml version="1.0" ?>', '<?xml version="1.0" encoding="utf-8"?>')
    # print(__cadena__)
    f = open(__OKFileName__, 'w')
    f.write(__cadena__)
    f.close()
    

def XML_RECEIVETASK_Generator(__RECEIVETASK_dict__, __ParameterFileCount__):

    __ReceiveFileName__ = __RECEIVETASK_dict__['ReceiveFileName'][__ParameterFileCount__]
    __RECEIVETASK_Keys__ = []
    __RECEIVETASK_Valores__ = []

    [__RECEIVETASK_Keys__.append(i) for i in __RECEIVETASK_dict__.keys()]
    [__RECEIVETASK_Valores__.append(__RECEIVETASK_dict__[__RECEIVETASK_Keys__[i]][__ParameterFileCount__]) for i in range(len(__RECEIVETASK_Keys__))]

    RECEIVETASK = Element('RECEIVETASK')

    __FileHeader__ = SubElement(RECEIVETASK, 'FileHeader')
    __FileBody__ = SubElement(RECEIVETASK, 'FileBody')

    for i in range(len(__RECEIVETASK_Keys__)):
        if i <= 4:
            __fild__ = __RECEIVETASK_Keys__[i]
            __fild__ = SubElement(__FileHeader__, __fild__)
            __fild__.text = __RECEIVETASK_Valores__[i]

        if i > 4 and i < len(__RECEIVETASK_Keys__) - 1:
            __fild__ = __RECEIVETASK_Keys__[i]
            __fild__ = SubElement(__FileBody__, __fild__)
            __fild__.text = __RECEIVETASK_Valores__[i]

    __cadena__0 = prettify(RECEIVETASK)
    __cadena__ = __cadena__0.replace('<?xml version="1.0" ?>', '<?xml version="1.0" encoding="utf-8"?>')
    f = open(__ReceiveFileName__, 'w')
    f.write(__cadena__)
    f.close()


def files_organizer(__CPLAN_extract__, __RecPass__):
    injection_files_path = directories_builder(__CPLAN_extract__)['satellite_Plan']
    reception_files_path = directories_builder(__CPLAN_extract__)['station_Plan']

    s_plan_files = []
    s_plan_files.append(__CPLAN_extract__['PlanFileName'])
    for i in SETPARAS_builder(__CPLAN_extract__)['ParameterFileName']:
         s_plan_files.append(i)
    s_plan_files.append(OK_builder(__CPLAN_extract__)['OKFileName'])
    r_plan_files = RECEIVETASK_builder(__CPLAN_extract__, __RecPass__)['ReceiveFileName']

    for i in s_plan_files:
         os.rename(i, injection_files_path + '/' + i)
    for i in r_plan_files:
         os.rename(i, reception_files_path + '/' + i)