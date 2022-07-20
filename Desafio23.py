numero = input ('Digite um numero de 0 a 9999 colocando todos os numeros: ')

print('O numero escolhido foi {}'.format(numero))

esp = ' '.join(numero)

div = esp.split()

print('Unidade: {}'.format(div[3]))

print('Dezena: {}'.format(div[2]))

print('Centena: {}'.format(div[1]))

print('Milhar: {}'.format(div[0]))