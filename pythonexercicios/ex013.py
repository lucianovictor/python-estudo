salario= float(input('Qual o salario do funcionario? R$'))
novo= salario + (salario * 15 / 100)
print('Um funcionario que ganhava R$ {:.2f} com aumento de 15%, passa a receber R$ {:.2f}'.format(salario, novo))
