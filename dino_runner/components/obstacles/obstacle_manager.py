import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Birds
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        n = self.geranumero()
        if len(self.obstacles) == 0:
            if n >= 1 and n <= 32:    
                self.obstacles.append(Cactus(SMALL_CACTUS[random.randint(0, 2)]))
            elif n >= 33 and n <= 65:
                self.obstacles.append(Cactus(LARGE_CACTUS[random.randint(0, 2)]))
            else:
                self.obstacles.append(Birds(BIRD[0]))


        for obstacle in self.obstacles:
            if isinstance(obstacle, Birds):
                obstacle.update(game.game_speed, self.obstacles, True)
            else:
                obstacle.update(game.game_speed, self.obstacles, False)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False  
        
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def geranumero(self):
       return random.randint(1, 99)