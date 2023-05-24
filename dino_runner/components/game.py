import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, MOUNTAIN, CLOUD, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE
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
        self.x_pos_mountain = -10
        self.y_pos_mountain = -40
        self.x_pos_cactus1 = 0
        self.x_pos_cactus2 = 400
        self.x_pos_cactus3 = 800
        self.x_pos_cactus4 = 1200
        self.x_pos_cactus5 = 1600
        self.x_pos_cactus6 = 2000


        self.executing = False
        
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.score = 0
        self.death_count = 0
        
        self.cloud_y_pos = random.randint(100, 250)
        self.cloud_x_pos = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        
    def execute(self):
        self.executing = True
        while self.executing:
            
            if not self.playing:
                self.display_menu()
        
        pygame.quit()    
    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
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
        self.obstacle_manager.update(self)

        self.update_score()
        self.update_speed()
        self.obstacle_manager.update(self)
        
    def update_score(self):
        self.score+=1
        
    def update_speed(self):
        if self.score % 100 == 0:
            self.game_speed += 10
        
    def draw(self):
        self.fps += 0.02
        self.clock.tick(self.fps)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_simple_cloud()
        self.player.draw(self.screen)
        self.draw_score()
        self.obstacle_manager.draw(self.screen)
        
        pygame.display.flip()

    def display_menu(self):
        self.screen.fill((255, 255, 255))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2
        
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render("Press any key to start", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x_text_pos, y_text_pos)
        
        self.screen.blit(text, text_rect)
        print(self.death_count)
        
        self.menu_events_handler()
        pygame.display.flip()
    
    def menu_events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()
                 
    
    def draw_score(self):
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        
        self.screen.blit(text, text_rect)
        
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

    def draw_simple_cloud(self):
        cloud_image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.cloud_x_pos, self.cloud_y_pos))
        
        if self.cloud_x_pos <= -cloud_image_width:
            self.cloud_x_pos = SCREEN_WIDTH + random.randint(0,50)
            self.cloud_y_pos = random.randint(100, 250)
            self.screen.blit(CLOUD, (self.cloud_x_pos, self.cloud_y_pos))
        
        self.cloud_x_pos -=self.game_speed
    
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 20
            
            
        
        
