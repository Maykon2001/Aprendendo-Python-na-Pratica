# Exercício 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:

peso = float(input("Qual seu peso ?(kg) "))
altura = float(input("Qual a sua altura ?(m) "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal.')
elif imc <= 30:
    print('Sobrepeso.')
elif imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')