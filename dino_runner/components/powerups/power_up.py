import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

# No geral, essa classe é uma classe pai que é usada para criar classes mais específicas de power-ups, como o escudo que é criado pela classe Shield, que é uma subclasse de PowerUp.
class PowerUp(Sprite):
    # O construtor da classe inicializa o PowerUp com uma imagem e um tipo (por exemplo, um escudo). Ele define a posição inicial do PowerUp na tela e também o tempo de duração do power-up.
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(125, 175)
        self.start_time = 0
        self.duration = random.randint(5, 10)
    
    # O método update é chamado a cada quadro e atualiza a posição do PowerUp, levando em conta a velocidade do jogo. Ele também verifica se o PowerUp saiu da tela, e se sim, o remove da lista de PowerUps.
    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()

    # O método draw desenha o PowerUp na tela.
    def draw(self, screen): 
        screen.blit(self.image, self.rect)