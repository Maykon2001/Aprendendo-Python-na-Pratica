#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de 
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:   

from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento

if idade <= 9:
    print('O atleta tem {} anos e está na categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e está na categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e está na categoria JÚNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e está na categoria SENIOR.'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria MASTER.'.format(idade))
    