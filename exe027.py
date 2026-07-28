# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Qual seu nome completo ? ')).strip()
nome = n.split() #Esta função divide o nome em listas numeradas a partir do 0.
print('Muito prezer em te conhecer !')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1])) #Esta função irá mostrar quantas posições tem o nome
