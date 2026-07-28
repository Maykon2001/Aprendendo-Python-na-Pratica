# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

a = int(input("Digite um número:"))
dobro = a * 2
triplo = a*3
raiz = a**(1/2)

print("O dobro de {} é {} o triplo é {} e a raiz quadrada é {:.2f}".format(a, dobro, triplo, raiz))