from datetime import datetime, timedelta
from xml.etree.ElementTree import Element, SubElement
from V2Gen.prettify import prettify


def BatchID_missions_table(__missions__, __BatchID__):
    __s_dia__ = timedelta(days=1)
    __s_hora__ = timedelta(hours=4, minutes=40)
    __dia__ = datetime.strptime(str(__BatchID__), '%Y%m%d')
    __diaA__ = __dia__ + __s_hora__
    __diaB__ = __dia__ + __s_dia__ + __s_hora__

    __misiones_BatchID__ = __missions__[
            (__missions__['Index'] >= 10) & \
            (__missions__['From Parent'] == 'From Parent VRSS-2') & \
            (__missions__['Date'] >= __diaA__) & \
            (__missions__['Date'] <= __diaB__)
        ].iloc[:, 0:35].reset_index()

# ------------------------------------------------------------------------
# Este segmento de código es el que permite imputar los valores de:
# workmode, __BatchID__ y PlanID
#
# Sin embargo BatchID es un parametro de la funcion. Para extraer este
# segmento y ejecutarlo en otro archivo, hay que definir una funcion que 
# calcule el BatchID e incorporarla en el nuevo archivo.
#

    __workmodes__ = {}

    for i in range(len(__misiones_BatchID__['Start Time (UTCG)'])):
        for j in range(len(__misiones_BatchID__['Start Time (UTCG)'])):
            if i != j:
                if __misiones_BatchID__['Start Time (UTCG)'][i] == __misiones_BatchID__['Start Time (UTCG)'][j]:
                    __workmodes__[i] = 'Realtime'
    
    for i in range(len(__misiones_BatchID__['Start Time (UTCG)'])):
        if i in __workmodes__.keys():
            continue
        elif 'Playback' in __misiones_BatchID__['To Object'][i]:
            __workmodes__[i] = 'Playback'
        else:
            __workmodes__[i] = 'Image'
    
    __misiones_BatchID__['Workmodes'] = [__workmodes__[i] for i in range(len(__workmodes__))]
    __misiones_BatchID__['BatchID'] = [__BatchID__ for i in range(len(__workmodes__))]

    __PlanID__ = []
    
    for i in range(len(__workmodes__)):
        if i == 0:
            j = 1
            __PlanID__.append(__BatchID__ * 1000000 + j)
        elif __misiones_BatchID__['Start Time (UTCG)'][i] != __misiones_BatchID__['Start Time (UTCG)'][i-1]:
            j = j + 1
            __PlanID__.append(__BatchID__ * 1000000 + j)
        else:
            __PlanID__.append(__BatchID__ * 1000000 + j)

    __misiones_BatchID__['PlanID'] = __PlanID__
    
# ------------------------------------------------------------------------
    
    return __misiones_BatchID__


def values_zero(__Access__, __Initial_codes__):
    
    __values_zero_dict__ = {}
    __batchid__ = __Access__['BatchID'][0]
    
    __dias__ = timedelta(days=1)
    __hora__ = timedelta(hours=12, seconds=1)
    __hora__0 = timedelta(hours=3)
    __fecha__ = datetime.strptime(str(__batchid__), '%Y%m%d')

    __renglones__ = len(__Access__)
    __n_realtimes__ = len(__Access__[
            __Access__['Workmodes'] == 'Realtime'
        ])

    PlanCount = int(__renglones__ - __n_realtimes__ / 2)

    __values_zero_dict__['MessageID'] = __Initial_codes__['MessageID']
    __values_zero_dict__['MessageCreateTime'] = \
        datetime.strftime(__fecha__ - __dias__ + __hora__, '%Y-%m-%dT%H:%M:%S')
    __values_zero_dict__['TaskID'] = str(__batchid__*1000000 + 10)
    __values_zero_dict__['FirstOrbitTime'] = \
        datetime.strftime(__fecha__ + __hora__0, '%Y-%m-%dT%H:%M:%S')

    __values_zero_dict__['PlanCount'] = str(PlanCount)
    __values_zero_dict__['PlanID'] = [str(__batchid__*1000000 + 1 + i) for i in range(PlanCount)]
    __values_zero_dict__['SatelliteID'] = ['VRSS-2' for i in range(PlanCount)]
    __values_zero_dict__['StationID'] = ['0' for i in range(PlanCount)]
    __values_zero_dict__['WorkMode'] = __Initial_codes__['WorkMode']

    __OrbitID__ = []
    for i in __values_zero_dict__['PlanID']:
        __values_PlanID__ = __Access__[__Access__['PlanID'] == int(i)].reset_index().iloc[0]
        __From_Pass__ = str(__values_PlanID__['From Pass'] + 2)
        __OrbitID__.append(__From_Pass__)    
    __values_zero_dict__['OrbitID'] = __OrbitID__
    
    __values_zero_dict__['CameraID'] = ['IRC,HRC' for i in range(PlanCount)]

    __PlaybackStartTime__ = []
    __PlaybackEndTime__ = []
    for i in __values_zero_dict__['PlanID']:
        __values_PlanID__ = __Access__[__Access__['PlanID'] == int(i)].reset_index().iloc[0]
        __workmode__ = __values_PlanID__['Workmodes']
        __start_time__ = datetime.strftime(__values_PlanID__['Start Time (UTCG)'], '%Y-%m-%dT%H:%M:%S')
        __end_time__ = datetime.strftime(__values_PlanID__['Stop Time (UTCG)'], '%Y-%m-%dT%H:%M:%S')
        if __workmode__ != 'Image':
            __PlaybackStartTime__.append(__start_time__)
            __PlaybackEndTime__.append(__end_time__)
        else:
            __PlaybackStartTime__.append('*')
            __PlaybackEndTime__.append('*')        
    __values_zero_dict__['TransStartTime'] = __PlaybackStartTime__
    __values_zero_dict__['TransEndTime'] = __PlaybackEndTime__

    __values_zero_dict__['IsBreakpoint'] = ['*' for i in range(PlanCount)]

    __DeleteFile__ = []
    for i in range(PlanCount):
        if __values_zero_dict__['WorkMode'][i] == '6':
            __DeleteFile__.append('-1')
        else:
            __DeleteFile__.append('*')
    __values_zero_dict__['DeleteFile'] = __DeleteFile__

    __RollAngle__ = []
    for i in __values_zero_dict__['PlanID']:
        __values_PlanID__ = __Access__[__Access__['PlanID'] == int(i)].reset_index().iloc[0]
        __workmode__ = __values_PlanID__['Workmodes']
        if __workmode__ != 'Playback':
            __values_PlanID__ = __Access__[
                    (__Access__['PlanID'] == int(i)) & \
                    (__Access__['Index'] == 10)    
                ].reset_index().iloc[0]
            
            __Angle__ = '{:.4f}'.format(__values_PlanID__['Roll Angle (deg)'])
            __RollAngle__.append(__Angle__)
        else:
            __RollAngle__.append('*')
    __values_zero_dict__['RollAngle'] = __RollAngle__

    __values_zero_dict__['YawAngle'] = ['*' for i in range(PlanCount)]
    __values_zero_dict__['PitchAngle'] = ['*' for i in range(PlanCount)]
    
    __ImageStartTime__ = []
    __ImageEndTime__ = []
    for i in __values_zero_dict__['PlanID']:
        __values_PlanID__ = __Access__[__Access__['PlanID'] == int(i)].reset_index().iloc[0]
        __workmode__ = __values_PlanID__['Workmodes']
        __start_time__ = datetime.strftime(__values_PlanID__['Start Time (UTCG)'], '%Y-%m-%dT%H:%M:%S')
        __end_time__ = datetime.strftime(__values_PlanID__['Stop Time (UTCG)'], '%Y-%m-%dT%H:%M:%S')
        if __workmode__ != 'Playback':
            __ImageStartTime__.append(__start_time__)
            __ImageEndTime__.append(__end_time__)
        else:
            __ImageStartTime__.append('*')
            __ImageEndTime__.append('*')    
    __values_zero_dict__['ImageStartTime'] = __ImageStartTime__
    __values_zero_dict__['ImageEndTime'] = __ImageEndTime__


    __FileName__ = []
    __Num_tomas__ = []
    for i in range(PlanCount):
        if __values_zero_dict__['WorkMode'][i] == '6':
            __FileName__.append('00H')
        elif __values_zero_dict__['ImageStartTime'][i] != '*' and \
            __values_zero_dict__['TransStartTime'][i] != '*':
            __FileName__.append('40H')
        elif __values_zero_dict__['ImageStartTime'][i] == '*' and \
            __values_zero_dict__['TransStartTime'][i] != '*':
            __FileName__.append('*')

        else:
            __FileName__.append(' ')
    __values_zero_dict__['FileName'] = __FileName__
    

    __ReplayFile__ = []
    __ImagingID__ = []
    __ImagingCount__ = []
    for i in __values_zero_dict__['ImageStartTime']:
        if i != '*':
            __ReplayFile__.append('*')
            __ImagingID__.append('0001')
            __ImagingCount__.append('1')
        else:
            # -------------------------------
            # Esto solo sucede cuando hay una sola imagen por descargar!.
            # Hay que depurar esta asignacion!
            __ReplayFile__.append('0')

            # Esta relacionada con los valores del FileName, pero eso no basta
            # debido a que la asignacion de los pases de descarga es esencialmente
            # arbitraria. De modo que tanto el FileName como el ReplayFile
            # hay de defnirlo desde la misma tabla! Queda para la proxima version.

            # -------------------------------
            __ImagingID__.append('*')
            __ImagingCount__.append('0')
    __values_zero_dict__['ReplayFile'] = __ReplayFile__
    __values_zero_dict__['ImagingID'] = __ImagingID__
    __values_zero_dict__['ImagingCount'] = __ImagingCount__


    return __values_zero_dict__

def XML_CPLAN2_generator(__CPLAN2_dict__):
     
    __CPLAN2_Keys__ = []
    __CPLAN2_Valores__ = []
    [__CPLAN2_Keys__.append(i) for i in __CPLAN2_dict__.keys()]
    [__CPLAN2_Valores__.append(__CPLAN2_dict__[__CPLAN2_Keys__[i]]) for i in range(len(__CPLAN2_Keys__))]

    __CPLAN2_PlanList_Keys__ = []
    __CPLAN2_PlanList_Valores__ = []
    [__CPLAN2_PlanList_Keys__.append(i) for i in __CPLAN2_dict__['PlanList'].keys()]
    [__CPLAN2_PlanList_Valores__.append(
            __CPLAN2_dict__['PlanList'][__CPLAN2_PlanList_Keys__[i]]) \
            for i in range(len(__CPLAN2_PlanList_Keys__))
        ]

    __CPLAN2_ImagingList_Keys__ = []
    __CPLAN2_ImagingList_Valores__ = []
    [__CPLAN2_ImagingList_Keys__.append(i) for i in __CPLAN2_dict__['PlanList']['ImagingList'].keys()]
    [__CPLAN2_ImagingList_Valores__.append(
            __CPLAN2_dict__['PlanList']['ImagingList'][__CPLAN2_ImagingList_Keys__[i]]) \
            for i in range(len(__CPLAN2_ImagingList_Keys__))
        ]


    __CPLAN2FileName__ = __CPLAN2_dict__['PlanFileName']

    CPLAN = Element('CPLAN')

    __FileHeader__ = SubElement(CPLAN, 'FileHeader')
    __FileBody__ = SubElement(CPLAN, 'FileBody')

    for i in range(len(__CPLAN2_Keys__) + 1):
        if i <= 4:
            __fild__ = __CPLAN2_Keys__[i]
            __fild__ = SubElement(__FileHeader__, __fild__)
            __fild__.text = __CPLAN2_Valores__[i]
            
        if i >= 5 and i <= 8:
            __fild__ = __CPLAN2_Keys__[i]
            __fild__ = SubElement(__FileBody__, __fild__)
            __fild__.text = __CPLAN2_Valores__[i]
        
        if i == 9:
            for j in range(len(__CPLAN2_PlanList_Valores__[0])):
                Planlist = SubElement(__FileBody__, 'PlanList')
                for k in range(len(__CPLAN2_PlanList_Keys__) - 1):
                    __fild__ = __CPLAN2_PlanList_Keys__[k]
                    __fild__ = SubElement(Planlist, __fild__)
                    __fild__.text = __CPLAN2_PlanList_Valores__[k][j]

                ImagingList = SubElement(Planlist, 'ImagingList')
                for k in range(len(__CPLAN2_ImagingList_Valores__)):
                    __fild__ = __CPLAN2_ImagingList_Keys__[k]
                    __fild__ = SubElement(ImagingList, __fild__)
                    __fild__.text = __CPLAN2_ImagingList_Valores__[k][j]


    __cadena__0 = prettify(CPLAN)
    __cadena__ = __cadena__0.replace('<?xml version="1.0" ?>', '<?xml version="1.0" encoding="utf-8"?>').replace('*', '')
    # print(__cadena__)
    f = open(__CPLAN2FileName__, 'w')
    f.write(__cadena__)
    f.close()   