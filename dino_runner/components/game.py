import pygame
import random

from dino_runner.utils.constants import HEART, FONT_STYLE, SMALL_CACTUS, LARGE_CACTUS, MOUNTAIN, CLOUD, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
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
        self.executing = False
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 100
        self.y_pos_cloud = 80
        self.x_pos_cloud2 = 900
        self.y_pos_cloud2 = 60
        self.x_pos_cloud3 = 1600
        self.y_pos_cloud3 = 90

        self.score = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
    
    def execute(self):
        self.executing = True
        while self.executing:
            
            if not self.playing:
                self.display_menu()
        
        pygame.quit() 

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()   
             

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
                
                
    def update(self):       
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.update_speed()
        self.obstacle_manager.update(self)

    def update_score(self):
        self.score+=1
        
    def update_speed(self):
        if self.score % 100 == 0:
            self.game_speed += 1
     
    def draw(self):
        self.clock.tick(self.fps)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.draw_speed()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        
        pygame.display.flip()

    def draw_score(self):       
        self.generate_text(f"Score: {self.score}", 22, 1000, 50)

    def draw_speed(self):
        self.generate_text(f"Km/h: {self.game_speed}", 22, 870, 50)

    def generate_text(self, textt, font_size, x, y):
        font = pygame.font.Font(FONT_STYLE, font_size)
        text = font.render(textt, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        
        self.screen.blit(text, text_rect)
      
    def draw_background(self):
        image_width = BG.get_width()
        self.printa(BG, image_width, self.x_pos_bg, -200, True)
        self.printa(CLOUD, image_width, self.x_pos_cloud, self.y_pos_cloud, True)
        self.printa(CLOUD, image_width, self.x_pos_cloud2, self.y_pos_cloud2, True)
        self.printa(CLOUD, image_width, self.x_pos_cloud3, self.y_pos_cloud3, True)
        if self.death_count <= 2:
            self.printa(HEART, image_width, 30, 30, True)
        if self.death_count <= 1:
            self.printa(HEART, image_width, 60, 30, True)
        if self.death_count == 0:
         self.printa(HEART, image_width, 90, 30, True)

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

    def display_menu(self):
        self.screen.fill((255, 255, 255))
        
        print(self.death_count)
         
        if self.death_count >= 1:
            self.secondary_menu_event_handler()
        else:
            self.main_menu_event_handler()
        pygame.display.flip()
    
    def main_menu_event_handler(self):
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2
        self.generate_text("Press any key to start", 22, x_text_pos, y_text_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()
            
    def secondary_menu_event_handler(self):
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2
        if self.death_count >= 1:
            self.generate_text("press space to restart ", 18, x_text_pos, y_text_pos - 60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.death_count = 0
                    self.reset_game()
                    self.run()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 15            
                 