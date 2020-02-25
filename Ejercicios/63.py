palabra = str(input('Escribe una palabra: '))
if palabra == palabra[::-1]:
	print('Es palindroma')
else:
	print('No es palindroma')
