#EP - Design de Software
#Equipe: Bruno Marques Li Volsi Falcao e Larissa Jordana de Paula Soares
#Data: 11/05/2021

import random
import colorama
colorama.init()

print('Paciência Acordeão \n\n Seja bem-vindo(a) ao jogo de Paciência Acordeão!\n O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.Existem apenas dois movimentos possíveis:\n1. Empilhar uma carta sobre a carta imediatamente anterior;\n2. Empilhar uma carta sobre a terceira carta anterior. \n\n Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n1. As duas cartas possuem o mesmo valor ou \n2. As duas cartas possuem o mesmo naipe. \nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.')



def cria_baralho():

    cartas=['A♠','A♥','A♦','A♣','2♠','2♥','2♦','2♣','3♠','3♥','3♦','3♣','4♠','4♥','4♦','4♣','5♠','5♥','5♦','5♣','6♠','6♥','6♦','6♣','7♠','7♥','7♦','7♣','8♠','8♥','8♦','8♣','9♠','9♥','9♦','9♣','10♠','10♥','10♦','10♣','J♠','J♥','J♦','J♣','Q♠','Q♥','Q♦','Q♣','K♠','K♥','K♦','K♣']

    random.shuffle(cartas)
    return cartas

# FUNCAO ORGANIZA AS ORDENS 

def display_baralho(baralho):
    for i,carta in enumerate(baralho,1):
        naipe = extrai_naipe(carta)
        if naipe == '♠':
            cor = colorama.Fore.BLUE
        elif naipe == '♥':
            cor = colorama.Fore.RED
        elif naipe == '♦':
            cor = colorama.Fore.WHITE
        elif naipe == '♣':
            cor = colorama.Fore.YELLOW
        print(f'{i}. {cor + carta + colorama.Fore.RESET}')

# FUNÇÃO QUE EXTRAI NAIPE
def extrai_naipe(cartas):
    return cartas[-1]

# FUNÇÃO QUE EXTRAI VALOR

def extrai_valor(valor):
    return valor[:-1:]

# FUNÇÃO MOSTRA MOVIMENTOS POSSIVEIS

def lista_movimentos_possiveis(baralho,indice):
    if indice == 0:
        return []
    resposta =[]

    carta = baralho[indice]
    naipe_carta = extrai_naipe(carta)
    valor_carta = extrai_valor(carta)

    if indice >= 1:
        carta1 = baralho[indice-1]
        naipe_carta1 = extrai_naipe(carta1)
        valor_carta1 = extrai_valor(carta1)
        if naipe_carta1 == naipe_carta or valor_carta1 == valor_carta:
            resposta.append(1)

            
    if indice >= 3:
        carta1 = baralho[indice-3]
        naipe_carta1 = extrai_naipe(carta1)
        valor_carta1 = extrai_valor(carta1)
        if naipe_carta1 == naipe_carta or valor_carta1 == valor_carta:
            resposta.append(3)
    return resposta

def possui_movimentos_possiveis(baralho):
    conta = 0
    while conta < len(baralho):
        
        movimento = lista_movimentos_possiveis(baralho,conta)
      
        if len(movimento) > 0:
            return True
        conta += 1
    return False


# FUNÇÃO QUE EMPILHA A CARTA

def empilha (baralho,origem, destino):

    carta_origem = baralho.pop(origem)
    baralho[destino]=carta_origem
    return baralho

def pergunta_escolha(pergunta,minimo,maximo):
    resposta = input(pergunta)
    if not resposta == '':
        numero = int(resposta)
        if numero >= minimo and numero <= maximo:
            return numero
    print('numero invalido')
    pergunta_escolha(pergunta,minimo,maximo)

baralho = cria_baralho()

inicio = input('Deseja jogar?(s ou n) ')

while inicio == 's':
    baralho = cria_baralho()
    while possui_movimentos_possiveis(baralho) == True:

        print('situação Atual:')

        display_baralho(baralho)
        escolha = pergunta_escolha(f'Escolha uma carta de 1 a {len(baralho)}: ',1,len(baralho))-1

        movimentos = lista_movimentos_possiveis(baralho, escolha)

        if len(movimentos) == 1:
            empilha(baralho,escolha,escolha - movimentos[0])
        elif len(movimentos) > 1:
            baralho_movimento = [baralho[escolha - i] for i in movimentos]
            display_baralho(baralho_movimento)
            destino = pergunta_escolha('Qual voce gostaria de empilhar: ',1,len(movimentos))-1
            empilha(baralho,escolha,escolha - movimentos[destino])
        else:
            print(f'voce nao pode escolher a carta {escolha + 1}, escolha novamente:')
    

    if possui_movimentos_possiveis(baralho) == True:
        print('Parabens você ganhou!')
        inicio = input('Gostaria de jogar novamente(s ou n): ')
    else:
        print('Você perdeu :(')
        inicio = input('Gostaria de jogar novamente(s ou n): ')
if inicio == 'n':

    print('OK:(. Nos vemos na próxima! Bye!')