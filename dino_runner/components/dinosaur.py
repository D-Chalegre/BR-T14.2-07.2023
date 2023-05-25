import pygame
import time

from dino_runner.utils.constants import RUNNING_HAMMER, DUCKING_HAMMER, JUMPING_HAMMER, HAMMER_TYPE, JUMPING_SHIELD, DUCKING_SHIELD, RUNNING_SHIELD, SHIELD_TYPE, DEFAULT_TYPE, SCREEN_WIDTH, RUNNING, JUMPING, DUCKING

Y_POS = 375
Y_POS_DUCK = 413
JUMP_VEL = 8.5
WALK = 5

RUN_IMG = {DEFAULT_TYPE: RUNNING, HAMMER_TYPE: RUNNING_HAMMER,
           DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}

DUCK_IMG = {DEFAULT_TYPE: DUCKING, HAMMER_TYPE: DUCKING_HAMMER,
            DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}

JUMP_IMG = {DEFAULT_TYPE: JUMPING, HAMMER_TYPE: JUMPING_HAMMER,
            DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}

class Dinosaur:
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[DEFAULT_TYPE][0]
        self.dino_rect = self.image.get_rect()

        self.buff1 = False
        self.buff2 = False

        self.has_power_up = False
        self.power_up_time_up = 0

        self.dino_rect.x = 10
        self.dino_rect.y = Y_POS
        
        self.step_count = 0
        
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        
        self.jump_vel = JUMP_VEL
    
    def update(self, user_input):
        valid = True
        if user_input[pygame.K_UP] and self.dino_rect.y == Y_POS:
            self.dino_run = False
            self.dino_jump = True
        elif not self.dino_jump:
            self.dino_run = True
        if user_input[pygame.K_DOWN]:
            self.dino_duck = True
            self.dino_run = False
        if user_input[pygame.K_LEFT] and self.dino_rect.x > 7:
            self.dino_rect.x -= 7
        if user_input[pygame.K_RIGHT] and self.dino_rect.x < 1000:
            self.dino_rect.x += 7
            
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if self.step_count > 9:
            self.step_count = 0

    
    def run(self):
        self.image = RUN_IMG[self.type][self.step_count//5]
        if self.image == RUN_IMG[HAMMER_TYPE][0]:
            self.buff1 = True
            self.buff2 = False
        if self.image == RUN_IMG[DEFAULT_TYPE][0]:
            self.buff1 = False
            self.buff2 = False
        if self.image == RUN_IMG[SHIELD_TYPE][0]:
            self.buff2 = True
            self.buff1 = False

        self.dino_rect.y = Y_POS
        
        self.step_count+=1
    
    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_count//5]
        if self.image == DUCK_IMG[HAMMER_TYPE][0]:
            self.buff1 = True
            self.buff2 = False
        if self.image == DUCK_IMG[DEFAULT_TYPE][0]:
            self.buff1 = False 
            self.buff2 = False
        if self.image == DUCK_IMG[SHIELD_TYPE][0]:
            self.buff2 = True
            self.buff1 = False
        self.dino_rect.y = Y_POS_DUCK
        
        self.step_count+=1
    
    def jump(self):
        self.image = JUMP_IMG[self.type]
        
        self.dino_rect.y -= self.jump_vel*4
        self.jump_vel -= 0.8
            
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect_y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL
           
    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x, self.dino_rect.y))
        