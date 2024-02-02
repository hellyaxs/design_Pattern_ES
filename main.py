from time import sleep
from src import WarII,jogador
import random


if '__main__' == __name__:
    # instancia do jogo #
    jogo = WarII(True, [])
    
    # instancias dos jogadores #    
    player1 = jogador('Jogador 1', jogo)
    player2 = jogador('Jogador 2',jogo)
    player3 = jogador('Jogador 3', jogo)

    # jogadores notificam ao jogo que estão prontos #
    player1.notify_subscribers()
    player2.notify_subscribers()
    player3.notify_subscribers()

    # jogo notifica aos jogadores que o jogo começou #
    jogo.add_subscriber(player1)
    jogo.add_subscriber(player2)
    jogo.add_subscriber(player3)
    jogo.notify_subscribers('o jogo começou!')

    # sleep de jogo #
    print('Jogo em andamento...')
    print('...')
    sleep(3)

    # jogo notifica aos jogadores que o jogo terminou #
    numero_aleatorio = random.randint(1, 3)
    print(f'numero aleatorio: {numero_aleatorio}')
    if numero_aleatorio == 1:
        jogo.notify_subscribers(f'o jogo terminou! e jogador {player1.nome} ganhou!')
    elif numero_aleatorio == 2:
        jogo.notify_subscribers(f'o jogo terminou! e jogador {player2.nome} ganhou!')
    else:
        jogo.notify_subscribers(f'o jogo terminou! e jogador {player3.nome} ganhou!')