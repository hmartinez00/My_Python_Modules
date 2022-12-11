import os
import subprocess

# --------------------------------------------
def project_route(__dir_dist, __project):
    try:
        __libs = os.listdir(__dir_dist)
        __tar_poject = [i for i in __libs if __project in i] 

        return __dir_dist + '/' + __tar_poject[-1]
    except:
        return None

# --------------------------------------------

project = input('Introduzca el nombre del proyecto a crear/actualizar: ')
dir_dist = 'dist'


# --------------------------------------------

tar_poject = project_route(dir_dist, project)

if tar_poject != None:

    shell_order = [
        'clear',
        'python setup.py sdist',
        'pip install ' + tar_poject,
    ]

    for i in shell_order:
        subprocess.run(i)

else:
    print('El paquete no fue encontrado!')

# --------------------------------------------