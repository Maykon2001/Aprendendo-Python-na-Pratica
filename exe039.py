from datetime import date

ano_atual = date.today().year
dt_nasc = int(input('Qual seu ano de nascimento ? (Apenas número): '))
sexo = str(input('Qual o sexo? H/M: ')).strip().upper()

if sexo == 'M':
    print('Mulheres não precisam faze o alistamento militar obrigatório')
else:
    idade = ano_atual - dt_nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(dt_nasc, idade, ano_atual))
    
    if idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        
