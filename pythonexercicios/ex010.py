real= float(input('Quanto dinheiro você tem na carteira? R$'))
dolar= real / 5.69
euro= real/ 6.79
libra = real/ 7.82
print('Com R$ {} você pode comprar US${:.2f} {:.2f}€$ {:.2f}£$'.format(real, dolar, euro, libra))
