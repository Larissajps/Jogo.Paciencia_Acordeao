#EP - Design de Software
#Equipe: Bruno Marques Li Volsi Falcao e Larissa Jordana de Paula Soares
#Data: 11/05/2021

import random
import colorama
colorama.init()

print('Paciência Acordeão \n\n Seja bem-vindo(a) ao jogo de Paciência Acordeão!\n O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.Existem apenas dois movimentos possíveis:\n1. Empilhar uma carta sobre a carta imediatamente anterior;\n2. Empilhar uma carta sobre a terceira carta anterior. \n\n Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n1. As duas cartas possuem o mesmo valor ou \n2. As duas cartas possuem o mesmo naipe. \nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. \nAperte [Enter] para iniciar o jogo...')



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

naipe = []
valor =[]
for i in range(0,len(baralho)):
    extrai_naipe = baralho[i][-1]
    naipe.append(extrai_naipe)

    
    if len(baralho[i]) > 2:
        valor_extraido = baralho[i][0] + baralho[i][1]
        valor.append(valor_extraido)
    else:
        valor_extraido = baralho[i][0]
        valor.append(valor_extraido)
print (valor)
print(naipe)

escolha = int(input('Escolha uma carta(1-52): '))
for carta in dic.keys():
    if escolha == carta:
        a = dic[carta]
        print(a)
