# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar 
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não
# pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor do salário: R$ '))
anos = int(input('Digite em quantos anos pretende pagar: '))
prestacao = casa / (anos * 12)
porcentagem = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}'.format(casa, anos, prestacao))
if prestacao <= porcentagem:
    print('Emperestimo aprovado!')
else:
    print('Emprestimo negado!')