from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from dino_runner.utils.constants import HAMMER
import random
class Missel(Obstacle):
    def __init__(self, image):
        super().__init__(image)  
        self.rect.x = SCREEN_WIDTH 
        self.rect.y = -100