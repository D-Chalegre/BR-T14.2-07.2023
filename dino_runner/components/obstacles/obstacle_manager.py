import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Birds
from dino_runner.components.obstacles.missel import Missel
from dino_runner.components.obstacles.meteor import Meteor
from dino_runner.utils.constants import DINO_DEAD, METEOR, MISSEL, BIRD, LARGE_CACTUS, SMALL_CACTUS
from dino_runner.utils.sons import IMPACTO

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        n = self.geranumero()
        if len(self.obstacles) == 0:
            if n >= 1 and n <= 19: 
                self.obstacles.append(Cactus(SMALL_CACTUS[random.randint(0, 2)]))
            elif n >= 20 and n <= 39:
                self.obstacles.append(Cactus(LARGE_CACTUS[random.randint(0, 2)]))
            elif n >= 40 and n <= 59:
                self.obstacles.append(Birds(BIRD))
            elif n >= 60 and n <= 79:
                self.obstacles.append(Meteor(METEOR))
            else:
                self.obstacles.append(Missel(MISSEL))


        for obstacle in self.obstacles:
            if isinstance(obstacle, Birds):
                obstacle.update(game.game_speed, self.obstacles, True, False)
            elif isinstance(obstacle, Meteor):
                if obstacle.valid == False:
                    self.obstacles.pop()
                obstacle.update(game.game_speed, self.obstacles, False, True)
            elif isinstance(obstacle, Missel):
                obstacle.update(game.game_speed, self.obstacles, False, True)
                if obstacle.valid == False:
                    self.obstacles.pop()
            else:
                obstacle.update(game.game_speed, self.obstacles, False, False)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                IMPACTO.play()
                if isinstance(obstacle, Birds):
                    self.collision(game, game.player.buff1)
                if isinstance(obstacle, Cactus):
                    self.collision(game, game.player.buff1)
                if isinstance(obstacle, Meteor):
                    self.collision(game, game.player.buff2)
                if isinstance(obstacle, Missel):
                    self.collision(game, game.player.buff2)

                self.reset_obstacles()
            #elif game.player.dino_rect.colliderect(obstacle.rect) and game.player.buff == True:

    def collision(self, game, buff):
        if buff == False:
            pygame.time.delay(500)
            if game.death_count == 2:
                game.player.image = DINO_DEAD
                if game.maior_score < game.score:
                    game.maior_score = game.score
                game.playing = False 
            game.death_count += 1

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def geranumero(self):
       return random.randint(1, 99)
    
    def reset_obstacles(self):
        self.obstacles.clear()