
from math import radians, sin, cos, tan
ângulo = float (input('Digite um ângulo que você deseja:'))
seno = sin(radians(ângulo))
print('O ângulo de {} tem seno de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem tangente de {:.2f}'.format(ângulo,tangente))
