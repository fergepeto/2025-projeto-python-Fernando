'''
Aequivo de funções utilizadas]
2025/06/25
fernando
'''

#objetivo: criar um arquivo de funções que serão utilizadas em nossos projetos

#BIBLIOTECAS
from random import randint #importa a função randint da biblioteca random

#CONSTANTES
TAM = int(30) #tamanho da tela
MAR = int(2) #margem da mensagens
CAR = '-' #caracter utilizado para desenhar as linhas

#VARIAVEIS

#LISTAS



#FUNÇÔES
#função para limpar a tela
def limpatela():
    print('\n' * TAM)
limpatela()

#função de mostrar uma msg 
def mostraline ():
    print(f'{CAR}' * TAM)

#mostrar uma msg no centro
def msgcenter(msg):
    print(f'{CAR} {msg:<{TAM-MAR-MAR}} {CAR}')

#mostrar uma msg a esquerda
def msgleft(msg):
    print(f'{CAR} {msg:<{TAM-MAR-MAR}}{CAR}')

#mostrar cabeçalho do jogo
def mostrarcabecalho(msgs):
    mostraline()
    for msg in msgs:
        msgcenter(msg)
    mostraline()

#mostra menu
def mostrarmenu(msgs):
    mostraline()
    for msg in msgs:
        msgleft(msg)
    mostraline()

#função para sortera o numero
def sortnum(limite):
    key = randint(1, limite)
    return key

#função de validar as entradas
def validavalue(resp, opcoes):
    if resp in opcoes:
        return True
    else:
        msgs = [f'{resp} não é uma opção válida!',
                f'Escolha uma das opções: {opcoes}']
        mostrarmenu(msgs)
        return False

#função para obter a entrada do usuário
def getvalue(msg):
    resp = input(f'{CAR}  {msg}: ').strip()
    return resp

#função para mostrar dica
def mosrtardica (resp, key):
    if resp > key:
        mostrarcabecalho(['Dica: O número é menor'])
    else:
        mostrarcabecalho(['Dica: O número é maior'])

#perguntar se quer jogar novamente
def playagain():
        opcoes = ['1', '0']
        mostrarcabecalho(['Deseja jogar novamente?', '[1] SIM', '[0] NÃO'])
        resp = getvalue('escolha sua opção')
        return resp =='1'

