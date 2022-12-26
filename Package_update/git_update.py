import os
from Pku_module.Package_update_module import auto_commit
from General_Utilities.option_list import option_list
from Pku_module.Package_update_module import listar_paquetes

# pregunta1 = input('Desea actualizar un paquete distribuible? (S/N): ')

# if pregunta1 == 's' or pregunta1 == 'S':
#     opciones = listar_paquetes()
#     project = option_list(opciones)
#     auto_commit(project)

# else:    
#     pregunta2 = input('Desea actualizar un proyecto? (S/N): ')

#     if pregunta2 == 's' or pregunta2 == 'S':
os.chdir('..')
opciones = os.listdir()
project = option_list(opciones)
auto_commit(project)