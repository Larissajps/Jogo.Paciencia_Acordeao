#EP - Design de Software
#Equipe: Bruno Marques Li Volsi Falcao e Larissa Jordana de Paula Soares
#Data: 11/05/2021

import random

print('Paciência Acordeão \n\n Seja bem-vindo(a) ao jogo de Paciência Acordeão!\n O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.Existem apenas dois movimentos possíveis:\n1. Empilhar uma carta sobre a carta imediatamente anterior;\n2. Empilhar uma carta sobre a terceira carta anterior. \n\n Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n1. As duas cartas possuem o mesmo valor ou \n2. As duas cartas possuem o mesmo naipe. \nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. \nAperte [Enter] para iniciar o jogo...')

############################### codigos feitos na academia python ############################

# def cria_baralho():
#     cartas=['A♠','A♥','A♦','A♣','2♠','2♥','2♦','2♣','3♠','3♥','3♦','3♣','4♠','4♥','4♦','4♣','5♠','5♥','5♦','5♣','6♠','6♥','6♦','6♣','7♠','7♥','7♦','7♣','8♠','8♥','8♦','8♣','9♠','9♥','9♦','9♣','10♠','10♥','10♦','10♣','J♠','J♥','J♦','J♣','Q♠','Q♥','Q♦','Q♣','K♠','K♥','K♦','K♣']

#     random.shuffle(cartas)
#     return cartas


###############################
# def extrai_naipe(carta):
#     return carta[-1]
#####################################
# def extrai_valor(valor):
#     return valor[:-1:]
#######################################
# def lista_movimentos_possiveis(baralho,indice):
#     if indice == 0:
#         return []
#     resposta =[]

#     carta = baralho[indice]
#     naipe_carta = extrai_naipe(carta)
#     valor_carta = extrai_valor(carta)

#     if indice >= 1:
#         carta1 = baralho[indice-1]
#         naipe_carta1 = extrai_naipe(carta1)
#         valor_carta1 = extrai_valor(carta1)
#         if naipe_carta1 == naipe_carta or valor_carta1 == valor_carta:
#             resposta.append(1)

            
#     if indice >= 3:
#         carta1 = baralho[indice-3]
#         naipe_carta1 = extrai_naipe(carta1)
#         valor_carta1 = extrai_valor(carta1)
#         if naipe_carta1 == naipe_carta or valor_carta1 == valor_carta:
#             resposta.append(3)
#     return resposta

# ############ FUNÇÃO MOVIMENTOS POSSIVEIS 
# def possui_movimentos_possiveis(baralho):
#     conta = 0
#     while conta < len(baralho):
        
#         movimento = lista_movimentos_possiveis(baralho,conta)
      
#         if len(movimento) > 0:
#             return True
#         conta += 1
#     return False
#######################################
# def empilha (baralho,origem, destino):

#     carta_origem = baralho.pop(origem)
#     baralho[destino]=carta_origem
#     return baralho


cartas=['A♠️','A♥️','A♦️','A♣️','2♠️','2♥️','2♦️','2♣️','3♠️','3♥️','3♦️','3♣️','4♠️','4♥️','4♦️','4♣️','5♠️','5♥️','5♦️','5♣️','6♠️','6♥️','6♦️','6♣️','7♠️','7♥️','7♦️','7♣️','8♠️','8♥️','8♦️','8♣️','9♠️','9♥️','9♦️','9♣️','10♠️','10♥️','10♦️','10♣️','J♠️','J♥️','J♦️','J♣️','Q♠️','Q♥️','Q♦️','Q♣️','K♠️','K♥️','K♦️','K♣️']
    
baralho=random.sample(cartas, len(cartas))
dic = {}
for i in range(0,len(baralho)):
    dic[i] = baralho[i]
print (dic)
# for i,value in enumerate(cartas,1):
#     print(i,value)

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
