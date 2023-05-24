import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, MOUNTAIN, CLOUD, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.fps = FPS
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        
        self.playing = False
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 100
        self.y_pos_cloud = 80
        self.x_pos_cloud2 = 900
        self.y_pos_cloud2 = 60
        self.x_pos_cloud3 = 1600
        self.y_pos_cloud3 = 90

        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()   
        pygame.quit()      

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                
                
    def update(self):       
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
     
    def draw(self):
        self.fps += 0.02
        self.clock.tick(self.fps)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        
        pygame.display.flip()

      
    def draw_background(self):
        image_width = BG.get_width()
        self.printa(BG, image_width, self.x_pos_bg, -200, True)
        self.printa(CLOUD, image_width, self.x_pos_cloud, self.y_pos_cloud, True)
        self.printa(CLOUD, image_width, self.x_pos_cloud2, self.y_pos_cloud2, True)
        self.printa(CLOUD, image_width, self.x_pos_cloud3, self.y_pos_cloud3, True)

        if self.x_pos_bg <= -image_width:
            self.printa(BG, image_width, self.x_pos_bg, -200, False)
            self.printa(CLOUD, image_width, self.x_pos_cloud3, self.y_pos_cloud3, False)
            self.printa(CLOUD, image_width, self.x_pos_cloud3, self.y_pos_cloud3, False)
            self.printa(CLOUD, image_width, self.x_pos_cloud3, self.y_pos_cloud3, False)

            self.x_pos_bg = 0
            self.x_pos_cloud = 100
            self.x_pos_cloud2 = 900
            self.x_pos_cloud3 = 1600

        self.x_pos_bg -= self.game_speed
        self.x_pos_cloud -= self.game_speed
        self.x_pos_cloud2 -= self.game_speed
        self.x_pos_cloud3 -= self.game_speed

    
    def printa(self, img, image_width, x, y, cond):
        if cond:
            self.screen.blit(img, (x, y))
        self.screen.blit(img, (image_width + x, y))