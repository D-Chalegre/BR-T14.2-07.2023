import pygame
from dino_runner.utils.constants import BALOES, DEFAULT_TYPE, HEART, FONT_STYLE, SMALL_CACTUS, LARGE_CACTUS, MOUNTAIN, CLOUD, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

class Draws:
    def draw_power_up_time(self, game):
        if game.player.has_power_up:
            time_to_show = round((game.player.power_up_time_up - pygame.time.get_ticks())/1000, 2)
            
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"Buff:{time_to_show}s", True, (255, 0, 0))
                
                text_rect = text.get_rect()
                text_rect.x = 700
                text_rect.y = 40
                
                game.screen.blit(text, text_rect)
                
            else:
                game.player.has_power_up = False
                game.player.type = DEFAULT_TYPE
    
    def generate_text(self, textt, font_size):
        font = pygame.font.Font(FONT_STYLE, font_size)
        text = font.render(textt, True, (0,0,0))
        return text
    
    def text_rect(self, x, y, game):
        text = self.generate_text(f"Score: {game.score}", 22)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        return text_rect


    def draw_score(self, game):       
        text = self.generate_text(f"Score: {game.score}", 22)
        text_rect = self.text_rect(1000, 50, game)
        game.screen.blit(text, text_rect)

    def draw_speed(self, game):
        text = self.generate_text(f"Km/h: {game.game_speed * 10}", 22)
        text_rect = self.text_rect(870, 50, game)
        game.screen.blit(text, text_rect)

    def draw_heart(self, game):
        if game.death_count <= 2:
            game.screen.blit(HEART, (30, 30))
        if game.death_count <= 1:
            game.screen.blit(HEART, (60, 30))
        if game.death_count == 0:
            game.screen.blit(HEART, (90, 30))

    def draw_baloes(self, game):
        image_width = BG.get_width()
        game.x_pos_cloud += 4
        game.x_pos_cloud3 += 4
        game.screen.blit(BALOES[0], (game.x_pos_cloud, game.y_pos_cloud))
        game.screen.blit(BALOES[2], (game.x_pos_cloud3, game.y_pos_cloud3))
        if game.x_pos_cloud <= -image_width:
            game.screen.blit(BALOES[0], (image_width + game.x_pos_cloud, game.y_pos_cloud))
            game.screen.blit(BALOES[2], (image_width + game.x_pos_cloud3, game.y_pos_cloud3))
            game.x_pos_cloud = 1100
            game.x_pos_cloud3 = 1900
        game.x_pos_cloud -= game.game_speed/3
        game.x_pos_cloud3 -= game.game_speed/2.7

    def draw_background(self, game):
        image_width = BG.get_width()
        game.screen.blit(BG, (game.x_pos_bg, -200))
        game.screen.blit(BG, (image_width + game.x_pos_bg, -200))
        if game.x_pos_bg <= -image_width:
            game.screen.blit(BG, (image_width + game.x_pos_bg, -200))           
            game.x_pos_bg = 0
        game.x_pos_bg -= game.game_speed
