# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

carro = int(input('Qual a velocidade do carro? '))
if carro > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h')
    multa = (carro - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
    