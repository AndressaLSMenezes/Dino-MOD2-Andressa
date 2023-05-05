import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "chris.png"))


RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Run/Run1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Run/Run2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Run/Run3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Run/Run4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Run/Run5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Run/Run6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Run/Run7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Run/Run8.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Shield/Run.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Run/Run2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Run/Run2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Chris/Jump/Jump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Chris/Shield/Jump.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Duck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Duck.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Shield/Duck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Shield/Duck.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Chris/Shield/Duck.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Rock.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Stem1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Stem2.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Rock.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Stem1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Stem2.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Circle/1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Circle/2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Circle/3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Circle/4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Circle/5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Circle/6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Circle/7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Circle/8.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/DirtRoad.jpg'))

WALLPAPER = pygame.image.load(os.path.join(IMG_DIR, "Other/Wallpaper/1.png"))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
