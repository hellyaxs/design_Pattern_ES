from .interfaces import Observer,Publisher

class jogador(Observer, Publisher):

    def __init__(self, nome, jogo=None):
        self.nome = nome
        self.jogo = jogo

    def update(self, observable, *args, **kwargs):
        print(f'jogador {self.nome} foi notificado por {observable} com a mensagem: {args[0]}')

    def add_subscriber(self, subscriber):
        self.jogo = subscriber

    def remove_subscriber(self, subscriber):
        self.jogo = None

    def notify_subscribers(self):
        if self.jogo:
            self.jogo.update(self.nome, f'eu estou pronto para jogar')
            
