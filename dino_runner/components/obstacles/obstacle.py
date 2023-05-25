from dino_runner.utils.constants import BIRD, SCREEN_WIDTH
import pygame
Y_POS = 380

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 100
        self.rect.y = 390
        self.direction = 'up'
        self.contador = 0
        self.cont = 0
        self.valid = True
    
    def update(self, game_speed, obstacles, cond1, cond2):
        self.cont += 1
        if self.cont >= 8:
            self.contador += 1
            self.cont = 0
        self.rect.x -= game_speed 

        if cond1:
            if self.direction == "up":
                self.rect.y -= 6
            if self.direction == "fixo":
                self.rect.y = 400
            if self.direction == "down":
                self.rect.y += 8

            if self.rect.y <= 100:
                self.direction = "down"
            if self.rect.y >= 400:
                self.direction = "fixo"

        if cond2:
            if self.rect.y < 350:
                self.valid = True
                self.rect.y += game_speed - 10
            else:
                self.valid = False
                   
        if self.rect.x <-self.rect.width:
            obstacles.pop()
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))