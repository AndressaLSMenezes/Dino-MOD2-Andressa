import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manager import PowerUpManager


class Game:
    # O método init() inicializa as variáveis e objetos necessários para o jogo, como a janela de exibição, o relógio para controlar o tempo de atualização, o jogador (Dinosaur), o gerenciador de obstáculos (ObstacleManager) e o gerenciador de power-ups (PowerUpManager).
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    # O método execute() é o loop principal do jogo, que executa enquanto a variável running for True. Dentro deste loop, a variável playing determina se o jogo está sendo executado ou não. Se a variável playing for False, o método show_menu() é chamado para exibir o menu principal do jogo.
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    # O método run() é chamado quando o jogador inicia ou reinicia o jogo, setando as variáveis e objetos necessários para o jogo e inicializando o loop do jogo. Dentro deste loop, os métodos events(), update() e draw() são chamados a cada frame para atualizar e desenhar os objetos na tela.
    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score= 0
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    # O método events() captura os eventos do teclado ou de mouse e define ações correspondentes. Neste caso, ele verifica se o evento é de saída da aplicação, para encerrar o jogo.
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    # O método update() atualiza os objetos do jogo a cada frame, incluindo o jogador, o gerenciador de obstáculos e o gerenciador de power-ups. Ele também atualiza a pontuação do jogo e a velocidade do jogo baseado na pontuação.
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    # O método update_score(self) é responsável por atualizar a pontuação do jogo e ajustar a velocidade do jogo. A cada vez que o método é chamado, a pontuação é incrementada em 1, e se a pontuação for um múltiplo de 100, a velocidade do jogo é aumentada em 5.
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    # O método draw() é responsável por desenhar os objetos do jogo na tela. Ele atualiza a janela de exibição, desenha o fundo, o jogador, os obstáculos, a pontuação e o tempo restante do power-up (se houver).
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    # O método draw_background(self) é responsável por desenhar o fundo do jogo. Ele usa a imagem armazenada na constante BG e desenha duas cópias lado a lado, movendo-as para a esquerda a cada atualização do jogo. Quando a primeira cópia sai da tela, ela é reposicionada para a direita da segunda cópia, para criar um efeito contínuo.
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
            self.x_pos_bg -= self.game_speed

    # O método draw_score(self) é responsável por desenhar a pontuação do jogador na tela. Ele usa o método draw_message_component do módulo text_utils para desenhar o texto "Pontos: " seguido da pontuação atual do jogo.
    def draw_score(self):
        draw_message_component(
            f"Pontos: {self.score}",
            self.screen,
            pos_x_center=1000,
            pos_y_center=50
        )
    
    # O método draw_power_up_time(self) é responsável por desenhar o tempo restante do power-up atual, caso o jogador tenha ativado um. Se o jogador tiver um power-up ativo, o método calcula quanto tempo resta até que ele expire e usa o método draw_message_component para desenhar o tempo restante na tela. Se o tempo restante for menor ou igual a zero, o power-up é desativado.
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks() / 1000, 2))
            if time_to_show >= 0:
                draw_message_component(
                f"{self.player.type.capitalize()} enable for {time_to_show} seconds", self.screen,
                font_size=18,
                pos_x_center=500,
                pos_y_center=40,
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
    
    # O método handle_events_on_menu() é um método auxiliar para lidar com os eventos no menu principal do jogo. Ele captura o evento de pressionar uma tecla e chama o método run() para iniciar o jogo.
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    # O método show_menu() exibe o menu principal do jogo. Ele verifica se o jogador perdeu, exibe a pontuação e a contagem de vidas, e exibe a opção de reiniciar o jogo. Ele também chama o método handle_events_on_menu() para lidar com eventos no menu.
    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.death_count == 0:
            draw_message_component("Pressione qualquer tecla para iniciar o jogo", self.screen)
        else :
            draw_message_component("Pressione qualquer tecla para reiniciar o jogo", self.screen, pos_y_center=half_screen_height + 140)

            draw_message_component(
                f"Sua pontuação: {self.score}",
                self.screen,
                pos_y_center=half_screen_height - 150
            )

            draw_message_component(
                f"Contagem de vida: {self.death_count}",
                self.screen,
                pos_y_center=half_screen_height - 100
            )
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 30))
            pygame.display.flip()
            self.handle_events_on_menu()