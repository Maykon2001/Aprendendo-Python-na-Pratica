# Exercício python 028: Escreva um progrma que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário 
# tentar descobrir qual foi o número escolhido pelo computador.

from random import randint
from time import sleep
computador = randint(0, 5) # O computador escolhe um número aleatório entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # O jogador tenta adivinhar o número escolhido pelo computador
print('PROCESSANDO...')
sleep(2) # Pausa o programa por 2 segundos para criar um efeito de suspense
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('GANHEI ! Eu pensei no número {} e não no número {}!'.format( computador, jogador))