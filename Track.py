import pygame as pg
import os
from Config import WIDTH

class Track:

    def __init__(self):
        self.x = 0
        self.y = 380
        self.TRACK = pg.image.load(os.path.join("Assets/Other", "Track.png"))

    def _update_x(self, speed):
        self.x -= speed // 12

    def draw(self, window, speed):
        window.blit(self.TRACK, (self.x, self.y))
        window.blit(self.TRACK, (WIDTH + self.x, self.y))
        if self.x <= -100:
            self.x = 0
            window.blit(self.TRACK, (WIDTH + self.x, self.y))
        self._update_x(speed)