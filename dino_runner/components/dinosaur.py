import pygame
from pygame.sprite import Group, Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD

DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
X_POS = 80
Y_POS = 310
Y_POS_DUCK = 340
JUMP_VEL = 8.5


class Dinosaur(Sprite):
    # O método init é responsável por inicializar o dinossauro e definir sua posição inicial na tela, seu tipo (padrão ou com escudo), a velocidade de salto, entre outros atributos.
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.dino_jump_vel = JUMP_VEL
        self.set_up_state()

    # O método set_up_state serve para definir o estado inicial do dinossauro, como a presença ou ausência de power-ups, escudos, e outras informações relacionadas.
    def set_up_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False 
        self.shield_time_up = 0

    # O método update é responsável por atualizar o estado do dinossauro a cada frame do jogo. Ele recebe como entrada um dicionário com as entradas do usuário e determina qual ação o dinossauro deve executar em resposta (correr, pular ou agachar). Também atualiza o estado do dinossauro de acordo com o tempo do jogo.
    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
        
        if self.step_index >= 9:
            self.step_index = 0

    # Os métodos run, jump e duck são responsáveis por atualizar a imagem do dinossauro de acordo com sua ação no jogo (correr, saltar ou agachar). Eles também atualizam a posição do dinossauro na tela.
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self): 
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.dino_jump_vel * 4
            self.dino_jump_vel -= 0.8
        if self.dino_jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.dino_jump_vel = JUMP_VEL
    
    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.dino_duck = False

    # O método draw é responsável por desenhar o dinossauro na tela. Ele recebe como entrada a tela onde o jogo está sendo exibido e utiliza o método blit do pygame para desenhar a imagem do dinossauro na posição correta.
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        
        

