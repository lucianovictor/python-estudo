km= float(input('Digite a quantidade de KM percorrido?'))
dias= int(input('Digite a quantidade de dias que o carro foi alugado?'))
pago= (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
