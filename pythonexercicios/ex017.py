from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi,hypot(hi)))
