'''
Projeto Python
2025/06/30
Fernando
'''
#espaço reservado para declaração das bibliotecas e funções
from modules import limpatela, mostrarcabecalho, mostrarmenu, validavalue
from random import shuffle

#variaveis
escolha = ''
resp = ''
pontos = 0
perguntas = ''

#listas
msg =''
msgsCab = ['Jogo QUIZ DOS ANIMAIS','Devenvolvido por Fernando']
msgsLevel = ['Preparado para reponder o QUIZ:',
             '[1] SIM', '[2] NÂO']

#funções do modules
limpatela()
mostrarcabecalho (msgsCab)
mostrarmenu (msgsLevel)

#validar a primeira escolha e invalidar se não for 1 ou 2 
escolha = input('-> ')
opcoes = ['1', '2']
while not validavalue(escolha, opcoes):
    escolha = input('-> ')
    #se escolher a oopção 2 mostra a msg de despedida e parar o codigo
if escolha == '2':
    print("vai embora então!")
    exit()
limpatela()

#função de todas as perguntas do quiz
def todas_perguntas():
    return [
        { "pergunta": 'Qual é o animal: Ele é o melhor amigo do homem ', "resposta": 'cachorro' },
        { "pergunta": 'Qual é o animal: Produtor de leite ', "resposta": 'vaca' },
        { "pergunta": 'Qual é o animal: Rei da selva ', "resposta": 'leão' },
        { "pergunta": 'Qual é o animal: Produtor de ovos ', "resposta": 'galinha' },
        { "pergunta": 'Qual é o animal: 100 homens vs 1 ', "resposta": 'gorila' },
        { "pergunta": 'Qual é o animal: Favorito do Lucas Neto ', "resposta": 'foca' },
        { "pergunta": 'Qual é o animal: Tem um desenho em que ele é rosa ', "resposta": 'pantera' },
        { "pergunta": 'Qual é o animal: Tem longas orelhas e come cenoura ', "resposta": 'coelho' },
        { "pergunta": 'Qual é o animal: Tem um longo pescoço ', "resposta": 'girafa' },
        { "pergunta": 'Qual é o animal: é muito gordo e tem um grande nariz ', "resposta": 'elefante' },
        { "pergunta": 'Qual é o animal: Que anda em alcateis e são divididos em alfa e beta ', "resposta": 'lobo' },
        { "pergunta": 'Qual é o animal: Gosta muito de Coca cola e vive no gelo ', "resposta": 'urso polar' },
        { "pergunta": 'Qual é o animal: Produtor de mel ', "resposta": 'abelha' },
        { "pergunta": 'Qual é o animal: Adora bananas ', "resposta": 'macaco' },
        { "pergunta": 'Qual é o animal: Tubarão de tenis ', "resposta": 'tralalelo tralala' },
        { "pergunta": 'Qual é o animal: Um cavalo com listras ', "resposta": 'zebra' },
        { "pergunta": 'Qual é o animal: Tem um casco e as vezes é ninja ', "resposta": 'tartaruga' },
        { "pergunta": 'Qual é o animal: Tem 8 patas e solta teia ', "resposta": 'aranha' },
        { "pergunta": 'Qual é o animal: Vive na Australia e pula muito ', "resposta": 'canguru' },
        { "pergunta": 'Qual é o animal: Sua carne é muito usada em feijoadas ', "resposta": 'porco' },
    ]
perguntas = todas_perguntas()

#codigo para aleatorizar as perguntas
shuffle(perguntas)
pontos = int(pontos)

#receber a msg do usuario e invalidar a msg do jogador se for um numero 
for p in perguntas:
    resposta_jogador = input(p["pergunta"])
    while resposta_jogador.isdigit():
        mostrarcabecalho(['Entrada inválida! Não digite números.'])
        #aumentar 1mponto a cada animal acertado e dizer que acetou e se não acertou        
        resposta_jogador = input(p["pergunta"])
    if resposta_jogador == p["resposta"]: 
        print("Correto!")
        pontos += 1
        print('\1')
    else:
        print("Errado! A resposta certa é:", p["resposta"])
        print('\1')

#mostrar o numero maximo de animais acertados
print(f'Você acertou {pontos} animais de 20')

