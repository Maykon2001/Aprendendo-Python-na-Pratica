# Exercício 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e 
#condição de pagamento:

print('{:=^40}'.format (' Loja do Maykin '))

preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO. 
[1] à vista dinheiro/pix.
[2] à vista cartão.
[3] 2x no cartão.
[4] 3x ou mais no catão.''')
opcao = int(input('Qual é a opção?: '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Sua compra será de R$ {:.2f} reais com 10% de desconto.'.format(total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Sua compra será de R$ {:.2f} reais no cartão à vista com 5% de desconto.'.format(total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} reais SEM JUROS.'.format(parcela))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas?: '))
    juros = preco * 20 / 100
    valParcela = (preco + juros) / parcelas
    if parcelas >= 3:
        total = preco + juros
        print('Sua compra será parcelada em {}x de R${:.2f} reais COM JUROS.'.format(parcelas,valParcela))
    else:
        print('Refaça a compra.')
else:
    total = None
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')

if total is not None:
    print('Sua compra de R${:.2f} reais vai custar R${:.2f} reais no final.'.format(preco,total))