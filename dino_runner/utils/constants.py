import pygame
import os


# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

FONT_STYLE = "freesansbold.ttf"

#Constante obstaculos
OBSTACLE_Y_POS = 325

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Other/pedra1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/pedra2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/pedra3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Other/pedra01.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/pedra02.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/pedra03.png")),
]

BALOES = [
    pygame.image.load(os.path.join(IMG_DIR, "Other/balao1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/balao2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/balao3.png")),
]

BIRD = pygame.image.load(os.path.join(IMG_DIR, "Other/passarinho.png"))

MISSEL = pygame.image.load(os.path.join(IMG_DIR, "Other/missel.png"))
METEOR = pygame.image.load(os.path.join(IMG_DIR, "Other/meteor.png"))

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
MOUNTAIN = pygame.image.load(os.path.join(IMG_DIR, 'Other/montanha.png'))
ROCHA = pygame.image.load(os.path.join(IMG_DIR, 'Other/rochaA.png')) 
FUNDO_MENU = pygame.image.load(os.path.join(IMG_DIR, 'Other/fundo_menu.jpg')) 
FUNDO_MENU2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/fundo_menu2.jpg')) 
DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDead.png')) 

GAME_OVER =  pygame.image.load(os.path.join(IMG_DIR, 'Other/game_over.gif')) 

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/mato2.jpg'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"

