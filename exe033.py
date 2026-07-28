# Exercício 33 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c =  int(input('Digite o terceiro valor: '))

if a < b and a < c: #verificando o menor valor
    print('O menor valor é {}'.format(a))
else:
    if b < c and b < a:
        print('O menor valor é {}'.format(b))
    else:
        print('O menor valor é {}'.format(c))
        if a > b and a > c: #verificando o maior valor
            print('O maior valor é {}'.format(a))
        else:
            if b > c and b > a:
                print('O maior valor é {}'.format(b))
            else:
                print('O maior valor é {}'.format(c))