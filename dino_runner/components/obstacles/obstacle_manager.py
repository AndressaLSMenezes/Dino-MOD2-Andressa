import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.when_appears = 0

    def update(self, game):
        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            if game.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                game.running = False

    def reset_obstacles(self): 
        self.obstacles = []
        self.when_appears = random.randint(200, 300) 

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)