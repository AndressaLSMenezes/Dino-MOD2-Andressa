import random
import pygame
from dino_runner.components.powerups.shield import Shield


class PowerUpManager:
    # É o construtor da classe e inicializa a lista de power-ups e a variável when_appears como zero.
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
    
    # Verifica se não há nenhum power-up na tela e se a pontuação do jogador é igual à variável 'when_appears'. Se isso ocorrer, uma instância de 'Shield' é criada e adicionada à lista de power-ups.
    def generate_power_up (self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_ups.append(Shield())
    
    # Atualiza o estado dos power-ups na lista. Para cada power-up, o método update é chamado para atualizar sua posição e verificar se ele colide com o jogador. Se ocorrer uma colisão, o escudo do jogador é ativado e a variável type do jogador é atualizada com o tipo do power-up. Além disso, a variável power_up_time do jogador é definida como o tempo atual do pygame em milissegundos mais a duração do power-up em segundos. Por fim, o power-up é removido da lista.
    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.chris_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

    # Desenha cada power-up na tela.
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    # Reinicia a lista de power-ups e define a variável when_appears como um valor aleatório entre 200 e 300.
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300) 