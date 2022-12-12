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