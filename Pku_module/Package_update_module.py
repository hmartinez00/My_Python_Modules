import os
import subprocess

def project_route(__dir_dist, __project):
    try:
        __libs = os.listdir(__dir_dist)
        __tar_poject = [i for i in __libs if __project in i] 

        return __dir_dist + '/' + __tar_poject[-1]
    except:
        return None

def listar_paquetes():
    __ejemplo_dir = os.getcwd()
    with os.scandir(__ejemplo_dir) as ficheros:
        subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]

    __paquetes = []
    for i in subdirectorios:
        if '.git' in i or \
            'dist' in i or \
            'Package_update' in i or \
            '.egg-info' in i:
            pass
        else:
            __paquetes.append(i)

    return __paquetes

def actualizar_paquetes(__dir_dist, __project):
    __tar_project = project_route(__dir_dist, __project)

    if __tar_project != None:

        shell_order = [
            'clear',
            'python setup.py sdist',
            'pip install ' + __tar_project,
        ]

        for i in shell_order:
            subprocess.run(i)

    else:
        print('El paquete no fue encontrado!')