import os
import subprocess
import json


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
        if '.egg-info' in i:
            __paquetes.append(i.split('.egg-info')[0])

    return __paquetes

def actualizar_setup(package):
    try:
        string = f'''from setuptools import setup

setup(
    name='{package['name']}',
    version='{package['version']}',
    description='{package['description']}',
    author='{package['author']}',
    author_email='{package['author_email']}',
    url='{package['url']}',
    packages={package['packages']}
)'''

        file = 'setup.py'
        f = open(file, 'w')
        f.write(string)
        f.close()

    except:
        print('Proyecto no encontrado!')

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