# Exercício 042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recuros de mostrar qe dtipo de triângulo seá formado: 

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acima PODEM FORMAR UM TRIÂNGULO!')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FOEMAR UM TRIÂNGULO!')