# Exercício Python 005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

sa = int(input("Digite um número:"))
print("O sucessor de {} é {} e o antecessor é {}".format(sa, (sa + 1), (sa - 1)))