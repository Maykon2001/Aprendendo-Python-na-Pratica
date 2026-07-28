# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input("Informe o preço do produto: R$"))
d = p * 0.05
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.".format(p, p-d))