opciones=[
	'Generar Setup',
	'Crear Proyecto',
	'Actualizar Proyecto',
]

Lista_opciones=''
for i in range(len(opciones)):
	Lista_opciones=Lista_opciones+\
	'\t{}. '.format(i+1) + opciones[i] + '\n'

str_menu='Acciones a Ejecutar: \n\n'+\
Lista_opciones
	
print(str_menu, end='\r')

opcion=input('\nSeleccione una opcion: ')

if opcion=='1':
	exec(open("setup_generator.py").read())
elif opcion=='2':
	exec(open("builder.py").read())
elif opcion=='3':
	print('Adios!')
else:
	print('\nOpcion Invalida! Repita la eleccion.\n')
	exec(open("menu.py").read())