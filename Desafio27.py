n = str(input('Digite seu nome completo: ')).strip()
n.title()

nome = n.split()

print('Seja bem vindo {}, prazer te conhecer.'.format(n))

print('Seu primeiro nome é {}'.format(nome[0]))

print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))