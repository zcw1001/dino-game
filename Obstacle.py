import pygame as pg
import random, os
from Config import WIDTH

SMALL_CACTUS = [pg.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pg.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pg.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pg.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pg.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pg.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.img_rect = self.image.get_rect()
        self.img_rect.x = WIDTH

    def _update_x(self, speed):
        self.img_rect.x -= speed // 12

    def draw(self, window, speed, offScreenCallback):
        window.blit(self.image, (self.img_rect.x, self.img_rect.y))
        self._update_x(speed)
        if self.img_rect.x < -100:
            offScreenCallback()


class SmallCactus(Obstacle):
    def __init__(self):
        i = random.randrange(0, 3)
        super().__init__(SMALL_CACTUS[i])
        self.img_rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self):
        i = random.randrange(0, 3)
        super().__init__(LARGE_CACTUS[i])
        self.img_rect.y = 300

class Pteranodon(Obstacle):
    def __init__(self):
        self.BIRD = [pg.image.load(os.path.join("Assets/Bird", "Bird1.png")),
                    pg.image.load(os.path.join("Assets/Bird", "Bird2.png"))]
        super().__init__(self.BIRD[0])
        i = random.randrange(0, 2)
        self.img_rect.y = (150, 250)[i]
        self.state_index = 0
    
    def draw(self, window, speed, callback):
        window.blit(self.BIRD[(self.state_index // 30) % 2], (self.img_rect.x, self.img_rect.y))
        self.state_index += 1
        self._update_x(speed)
        if self.img_rect.x < -100:
            callback()