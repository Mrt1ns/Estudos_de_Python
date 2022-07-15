from math import hypot

#Cateto Oposto
co = float(input('Digite o Cateto Oposto: '))

#Cateto Adjacente
ca = float(input('Digite o Cateto adjacente: '))

#Hipotenusa
hp = hypot(co, ca)

print(hp)