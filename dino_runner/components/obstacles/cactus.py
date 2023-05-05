import random

from dino_runner.utils.constants import  SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):

    CACTUS = [
        (SMALL_CACTUS, 325),
    ]

    def __init__(self):
        image, cactus_pos = self.CACTUS[0]
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = cactus_pos