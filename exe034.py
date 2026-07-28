# Exercício 34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input('Qual é o seu salário atual? R$ '))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('O seu salário com aumento é de R$ {:.2f}'.format(aumento))