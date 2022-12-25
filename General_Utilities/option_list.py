import os


def list_files(__dir):
    rutes = []
    os.chdir(__dir)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            ruta = os.path.join(root, name)
            rutes.append(ruta)
    
    return rutes

def list_dir(__dir):
    rutes = []
    os.chdir(__dir)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            ruta = os.path.join(root, name)
            rutes.append(ruta)
    
    return rutes


def option_list(__list):
    opciones=__list

    Lista_opciones=''
    for i in range(len(opciones)):
        Lista_opciones=Lista_opciones+\
        '\t{}. '.format(i+1) + opciones[i] + '\n'

    str_menu='Lista de opciones: \n\n'+\
    Lista_opciones
        
    print(str_menu, end='\r')

    opcion=input('\nSeleccione una opcion: ')

    project = opciones[int(opcion) - 1]

    return project