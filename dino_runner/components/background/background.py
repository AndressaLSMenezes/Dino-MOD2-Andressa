import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.transform = pygame.transform.scale(self.image, (1100, 600))
        self.rect = self.transform.get_rect()
        self.rect.left, self.rect.top = location