# Exercício 050 - Desenvolva um programa que leia seis número inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for c in range (1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Voçê informou {} números e a soma foi {}.'.format(cont, soma))