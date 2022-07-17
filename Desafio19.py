from random import choice

n1 = input('Digite um nome: ')
n2 = input('Digite outro nome: ')
n3 = input('Digite outro nome: ')
n4 = input('Digite outro nome: ')

lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print('O escolhido(a) foi {}'.format(escolhido))