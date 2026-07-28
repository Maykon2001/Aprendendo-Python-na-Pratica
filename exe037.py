num = int(input(' Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
      [ 1 ] converter para BINÁRIO
      [ 2 ] converter para OCATAL
      [ 3 ] converter para EXADECIAMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para OCATAL é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para EXADECIAMAL é igual a {}'.format(num, hex(num)))
else:    
    print('Opção inválida. Tente novamente.')