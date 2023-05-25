import random

from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = 150
        #tempo que eh criado o power_up
        self.start_time = 0
        self.direction = 'up'
        #duração em segundos
        self.duration = random.randint(5,10)
    
    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed

        if self.direction == 'up':
            self.rect.y -=  14
        if self.direction == 'down':
            self.rect.y +=  14

        if self.rect.y <= 100:
            self.direction = "down"
        if self.rect.y >= 300:
            self.direction = 'up'

        if self.rect.x < -self.rect.width:
            power_ups.pop()
            
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))