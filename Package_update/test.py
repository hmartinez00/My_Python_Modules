import os
from Pku_module.Package_update_module import listar_paquetes

ejemplo_dir = os.getcwd()
print(listar_paquetes(ejemplo_dir))