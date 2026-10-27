# Exercício 063 - Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos 
# de fibonacci. 
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print(23*'-')
print('Sequência de Fibonacci')
print(23*'-')

t1 = 0
t2 = 1
n = int(input('Quantos termos você quer mostrar? '))
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')