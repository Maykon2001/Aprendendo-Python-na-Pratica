# Exercício 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre os 
# 10 primeiros termos dessa progressão.

print(10 *'-=')
print('   Gerador de PA')
print(10 *'-=')

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo,decimo + razao,razao):
    print('{}'.format(c), end = '--')
print('ACABOU!!!')
        
        