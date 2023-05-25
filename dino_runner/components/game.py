import pygame
import random

from dino_runner.utils.sons import FINAL_GAME, SOM_DE_FUNDO, MENU, CLICK
from dino_runner.utils.constants import BALOES, DEFAULT_TYPE, HEART, FONT_STYLE, SMALL_CACTUS, LARGE_CACTUS, MOUNTAIN, CLOUD, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.menus import Menu
from dino_runner.components.draws import Draws
from dino_runner.components.updates import Updates
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
        self.power_up_manager = PowerUpManager()
        self.menu = Menu()
        self.updates = Updates()
        self.draws = Draws()
        
        self.playing = False
        self.executing = False

        self.game_speed = 15

        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 1100
        self.y_pos_cloud = 5
        self.x_pos_cloud2 = 2400
        self.y_pos_cloud2 = 60
        self.x_pos_cloud3 = 2100
        self.y_pos_cloud3 = 10

        self.score = 0
        self.maior_score = 0
        self.death_count = 0

        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.som_menu = False
        self.som_de_fundo = False
        
    
    def execute(self):
        self.executing = True
        while self.executing:       
            if not self.playing:
                self.menu.display_menu(self)
        
        pygame.quit() 

    def run(self):
        # Game loop: events - update - draw
        if self.som_de_fundo == False:
            SOM_DE_FUNDO.play()
            self.som_de_fundo = True
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()   
        else:
            pygame.time.delay(500)
            SOM_DE_FUNDO.stop()
            FINAL_GAME.play()
             

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
                
                
    def update(self):       
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.updates.update_score(self)
        self.updates.update_speed(self)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

     
    def draw(self):
        self.clock.tick(self.fps)
        self.screen.fill((255, 255, 255))
        self.draws.draw_background(self)
        self.draws.draw_score(self)
        self.draws.draw_speed(self)
        self.player.draw(self.screen)
        self.draws.draw_power_up_time(self)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draws.draw_baloes(self)
        self.draws.draw_heart(self)
        
        pygame.display.flip()

    def reset_game(self):
        self.click = False
        self.som_de_fundo = False
        self.som_menu = False
        self.obstacle_manager.reset_obstacles()
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 15            
                 