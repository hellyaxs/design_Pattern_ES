from typing import Type
from .interfaces import Observer,Publisher

class WarII(Publisher, Observer):

    def __init__(self, state: bool, jogadores: list):
        self.nome = 'War II'
        self.state = False
        self.jogadores = []
        
    def add_subscriber(self, jogador: Type[Observer]):
        self.jogadores.append(jogador)

    def notify_subscribers(self,mensagem: str):
        self.state = not self.state
        for jogador in self.jogadores:
            jogador.update(self.nome,mensagem)    
    
    def remove_subscriber(self, subscriber):
        self.jogadores.remove(subscriber)

    def update(self, observable, *args, **kwargs):
        print(f'jogo {self.nome} foi notificado por {observable} com a mensagem: {args[0]}')
    
 