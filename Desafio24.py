cidade = input('Digite o nome da sua cidade: ')

titulo = cidade.title()

div = titulo.split()

santa = ('Santa' in titulo[0:5])

certo = print('O primeiro nome da cidade {} e Santa: {}'.format(titulo, santa))