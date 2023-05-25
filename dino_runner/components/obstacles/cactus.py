
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import HAMMER

class Cactus(Obstacle):
    def __init__(self, image):
        super().__init__(image)      