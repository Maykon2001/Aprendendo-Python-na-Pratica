# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o nome completo: ')).strip()
print('O nome tem Silva? {}'.format('SILVA' in nome.upper()))