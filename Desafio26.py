frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes'. format(frase.count('A')+1))

print('A letra A se encontra na {} posição'.format(frase.find('A')+1))

print('A ultima letra A se encontra na posição {}'.format(frase.rfind('A')+1))