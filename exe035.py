#Exercício 35 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar 
# um triângulo.

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(int(input('Primeiro segmento: ')))
r2 = float(int(input('Segundo seguimento: ')))
r3 = float(int(input('Terceiro segmento: ')))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FOEMAR UM TRIÂNGULO!')
