import random

def cria_baralho():

    cartas=['A♠','A♥','A♦','A♣','2♠','2♥','2♦','2♣','3♠','3♥','3♦','3♣','4♠','4♥','4♦','4♣','5♠','5♥','5♦','5♣','6♠','6♥','6♦','6♣','7♠','7♥','7♦','7♣','8♠','8♥','8♦','8♣','9♠','9♥','9♦','9♣','10♠','10♥','10♦','10♣','J♠','J♥','J♦','J♣','Q♠','Q♥','Q♦','Q♣','K♠','K♥','K♦','K♣']

    random.shuffle(cartas)
    return cartas

def extrai_naipe(carta):
    return carta[-1]


def extrai_valor(valor):
    return valor[:-1:]


