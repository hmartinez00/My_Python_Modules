import os
import subprocess
from General_Utilities.cntrl_exit import salida

# --------------------------------------------
def project_route(__dir_dist, __project):
    try:
        __libs = os.listdir(__dir_dist)
        __tar_poject = [i for i in __libs if __project in i] 

        return __dir_dist + '/' + __tar_poject[-1]
    except:
        return None

# --------------------------------------------

project = input('Introduzca el nombre del proyecto: ')
dir_dist = 'dist'

# --------------------------------------------

tar_project = project_route(dir_dist, project)

if tar_project != None:

    shell_order = [
        'clear',
        'python setup.py sdist',
        'pip install ' + tar_project,
    ]

    for i in shell_order:
        subprocess.run(i)

else:
    print('El paquete no fue encontrado!')

# --------------------------------------------

salida("builder")