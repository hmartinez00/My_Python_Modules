def salida(__file_Name__):
	opcion=input('\n\nDesea continuar? (S/N): ')

	if opcion=='s' or opcion=='S':
		exec(open(__file_Name__ + '.py').read())
	else:
		# opcion=='n' or opcion=='N':
		exec(open('menu.py').read())
	# else:
		# exec(open('cntrl_exit.py').read())