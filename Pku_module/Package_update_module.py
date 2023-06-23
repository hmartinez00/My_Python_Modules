import os
import subprocess
from General_Utilities.option_list import list_files
from datetime import datetime as dt
from General_Utilities.fecha import BatchID, TimeID


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
            'cls',
            'python setup.py sdist',
            'pip install ' + __tar_project,
        ]

        for i in shell_order:
            subprocess.run(i, shell=True)

    else:
        print('El paquete no fue encontrado!')


def get_modified_files():
    output = subprocess.check_output(['git', 'status', '-s']).decode('utf-8').strip()
    lines = output.split('\n')
    files = [line.split()[1] for line in lines]
    return files


def auto_commit():

    ahora = dt.now()

    rutes = get_modified_files()

    # rutes = []
    # for i in list_files(__project):
    #     if '.git' in i:
    #         continue
    #     else:
    #         rutes.append(i)
    
    # rutes.append('.gitignore')


    total_add = 'git add '
    for i in rutes:
        total_add = total_add + ' ' + i
    print(total_add)

    commit_order = 'git commit -m "' + f'Version Estable {BatchID(ahora)} {TimeID(ahora)}' + '"'

    shell_order = [
        total_add,
        commit_order,
    ]

    for i in shell_order:
        subprocess.run(i, shell=True)