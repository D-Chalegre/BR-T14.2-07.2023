import random
import pygame
import time

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Birds
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


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
        if len(self.obstacles) == 0:
            option = random.randint(1,3)
            if option == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS[random.randint(0,2)]))
            elif option == 2:
                cactus = Cactus(LARGE_CACTUS[random.randint(0,2)])
                cactus.rect.y = 300# mudando a posição do cactus Largo
                self.obstacles.append(cactus)
            elif option == 3:
                self.obstacles.append(Bird(BIRD))
                
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
            
        
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def geranumero(self):
       return random.randint(1, 99)
            
    def reset_obstacles(self):
        self.obstacles.clear()
