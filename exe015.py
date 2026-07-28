# Exercício Python 015: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km = float(input("Informe a distância percorrida em km: "))
dias = int(input("Informe a quantidade de dias que o carro foi alugado: "))

preco = (60 * dias) + (0.15 * km)

print("O preço total a pagar pelo aluguel do carro é de R$ {:.2f}.".format(preco))