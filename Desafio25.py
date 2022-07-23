from unicodedata import name


nome = input('Digite seu nome: ')

print('No nome {} contém Silva: '.format(nome), 'Silva' in nome)