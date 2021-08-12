frase = str(input('Digite uma frase:')).lower().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('Qual posição aparece a letra A {}'.format(frase.find('a')+1))
print('Onde apareceu a ultima letra A {}'.format(frase.rfind('a')+1))
