import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH
import random

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(125, 175)
        self.start_time = 0
        self.duration = random.randint(5, 10)

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)