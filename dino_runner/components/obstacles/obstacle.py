from dino_runner.utils.constants import BIRD, SCREEN_WIDTH
import pygame
Y_POS = 380

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 390
        self.direction = 'up'
        self.contador = 0
        self.cont = 0
    
    def update(self, game_speed, obstacles, cond):
        self.cont += 1
        if self.cont >= 8:
            self.contador += 1
            self.cont = 0
        self.rect.x -= game_speed 

        if cond:
            if self.direction == "up":
                self.rect.y -= game_speed - 15
            else:
                self.rect.y += game_speed - 15

            if self.rect.y <= 150:
                self.direction = "down"
            elif self.rect.y >= 420:
                self.direction = "up"

            if self.image == BIRD[0]:
                if self.contador % 2 == 0:
                    self.image = BIRD[1]
            else:
                if self.contador % 2 != 0:
                    self.image = BIRD[0]
                   
        if self.rect.x <-self.rect.width:
            obstacles.pop()
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))