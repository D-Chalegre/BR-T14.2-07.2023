import pygame
import random

from dino_runner.utils.constants import MOUNTAIN, CLOUD, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.player = Dinosaur()
        
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 100
        self.y_pos_cloud = 80
        self.x_pos_cloud2 = 900
        self.y_pos_cloud2 = 60
        self.x_pos_cloud3 = 1600
        self.y_pos_cloud3 = 90
        self.x_pos_mountain = -10
        self.y_pos_mountain = -40

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
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        mountain = pygame.transform.scale(MOUNTAIN,(2580, 420))
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        self.clouds(image_width, self.x_pos_cloud, self.y_pos_cloud, True)
        self.clouds(image_width, self.x_pos_cloud2, self.y_pos_cloud2, True)
        self.clouds(image_width, self.x_pos_cloud3, self.y_pos_cloud3, True)
        self.screen.blit(mountain, (self.x_pos_mountain, self.y_pos_mountain))
        self.screen.blit(mountain, (image_width + self.x_pos_mountain, self.y_pos_mountain))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.clouds(image_width, self.x_pos_cloud3, self.y_pos_cloud3, False)
            self.clouds(image_width, self.x_pos_cloud3, self.y_pos_cloud3, False)
            self.clouds(image_width, self.x_pos_cloud3, self.y_pos_cloud3, False)
            self.screen.blit(mountain, (image_width + self.x_pos_mountain, self.y_pos_mountain))
            self.x_pos_bg = 0
            self.x_pos_cloud = 100
            self.x_pos_cloud2 = 900
            self.x_pos_cloud3 = 1600
            self.x_pos_mountain = -10
        self.x_pos_bg -= self.game_speed
        self.x_pos_cloud -= self.game_speed
        self.x_pos_cloud2 -= self.game_speed
        self.x_pos_cloud3 -= self.game_speed
        self.x_pos_mountain -= self.game_speed
    
    def clouds(self, image_width, x, y, cond):
        if cond:
            self.screen.blit(CLOUD, (x, y))
        self.screen.blit(CLOUD, (image_width + x, y))